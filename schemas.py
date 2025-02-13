from pydantic import BaseModel


class MessageRequest(BaseModel):
    user_id: str
    user_message: str


class MessageResponse(BaseModel):
    user_message: str
    bot_response: str
