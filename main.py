import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud
from schemas import MessageRequest, MessageResponse
from langchain_openai import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

load_dotenv()


Open_API_KEY = os.getenv("Open_API_KEY")

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Allow CORS for all origins (you can restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/history/{user_id}")
async def get_history(user_id: str, db: Session = Depends(get_db)):
    history = crud.get_message_history(db, user_id)
    if not history:
        raise HTTPException(
            status_code=404, detail="No message history found for this user."
        )
    return history


# Endpoint to send a message
# Endpoint to send a message
@app.post("/chat/", response_model=MessageResponse)
async def chat(request: MessageRequest, db: Session = Depends(get_db)):
    llm = ChatOpenAI(api_key=Open_API_KEY)  # Pass the OpenAI API key
    user_message = request.user_message
    user_id = request.user_id

    # Fetch message history for context
    history = crud.get_message_history(db, user_id)
    history_messages = " ".join(
        [f"User: {msg.user_message} Bot: {msg.bot_response}" for msg in history]
    )

    # Combine history with the current user message for context
    context = f"{history_messages} User: {user_message}"

    # Get response from LangChain using the context
    bot_response = llm(context)

    # Extract the content from the AIMessage object
    bot_response_content = (
        bot_response.content if hasattr(bot_response, "content") else str(bot_response)
    )

    # Save to database
    crud.save_message(db, user_id, user_message, bot_response_content)

    return {"user_message": user_message, "bot_response": bot_response_content}
