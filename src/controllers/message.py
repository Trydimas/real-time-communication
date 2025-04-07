from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.message import MessageResp, MessageSend, MessageRefactor, MessagesResp
from repositories import message
from db import get_session

router = APIRouter(
    prefix="/messages",
    tags=["message"]
)


# TODO AI, that check message in moment send

@router.get("/")
def get_all_messages(
        session: Session = Depends(get_session),
        last_key: str | None = None,
        limit: int = 10
) -> MessagesResp:
    return message.get_all_messages(session, last_key=last_key, limit=limit)


@router.get("/user/{user_id}")
def get_messages_by_user(
        user_id: str,
        session: Session = Depends(get_session)
) -> list[MessageResp]:
    return message.get_messages_by_user(user_id)


@router.get("/{message_id}")
def get_message_by_id(
        message_id: str,
        session: Session = Depends(get_session)
) -> MessageResp:
    return message.get_message_by_id(message_id)


@router.post("/")
def send_message(
        body: MessageSend,
        session: Session = Depends(get_session)
) -> MessageResp:
    return message.send_message(body)


@router.delete("/{message_id}")
def delete_message(
        message_id: str,
        session: Session = Depends(get_session)
) -> MessageResp:
    return message.delete_message(message_id)


@router.put("/{message_id}")
def refactor_message(
        message_id: str,
        body: MessageRefactor,
        session: Session = Depends(get_session)
) -> MessageResp:
    return message.refactor_message(message_id, body)
