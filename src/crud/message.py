from sqlalchemy.orm import Session, joinedload
from models.message import Message
from datetime import datetime

from schema.message import MessageResp
from crud.user import get_user_by_id
from models.user import User

def check_messages():
    pass


def get_all_messages(session: Session, *,
                     last_date: datetime | None = None,
                     limit: int = 100
                     ) -> list[MessageResp]:
    """List of messages by ascending"""

    messages = session.query(Message)
    order_messages = messages.order_by(Message.created_at.asc())
    filter_messages = order_messages.filter(Message.created_at > last_date) if last_date else order_messages
    limit_messages = filter_messages.limit(limit).all()
    return [MessageResp.model_validate(msg) for msg in limit_messages]


def get_date_by_key(session: Session,
                    *,
                    last_key: str | None = None
                    ) -> datetime | None:
    """Date will be using for comparison"""

    if not last_key:
        return None
    message = session.get(Message, last_key)
    return message.created_at  # type: ignore


def get_messages_by_user(session: Session,
                         *,
                         user_id: str,
                         limit: int = 100
                         ) -> MessageResp:
    #user = get_user_by_id(session, user_id=user_id)
    return




