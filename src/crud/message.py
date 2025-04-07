from schema.message import MessageResp
from sqlalchemy.orm import Session
from models.message import Message
from datetime import datetime


def get_all_messages(session: Session, *,
                     last_date: datetime | None = None,
                     limit: int = 100
                     ) -> list[MessageResp]:
    # TODO не возвращается нужный last_key

    messages = session.query(Message)
    order_messages = messages.order_by(Message.created_at.asc())
    filter_messages = order_messages.filter(Message.created_at > last_date) if last_date else order_messages
    limit_messages = filter_messages.limit(limit).all()
    return [MessageResp.model_validate(msg) for msg in limit_messages]


def get_date_by_key(session: Session,
                    *,
                    last_key: str | None = None
                    ) -> datetime | None:
    if not last_key:
        return None
    message = session.get(Message, last_key)
    return message.updated_at


def checked_messages():
    pass
