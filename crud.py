from sqlalchemy.orm import Session
from models import MessageHistory


def save_message(db: Session, user_id: str, user_message: str, bot_response: str):
    message = MessageHistory(
        user_id=user_id, user_message=user_message, bot_response=bot_response
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_message_history(db: Session, user_id: str):
    return db.query(MessageHistory).filter(MessageHistory.user_id == user_id).all()
