from sqlalchemy.orm import Session
from loguru import logger
from crud.message import get_date_by_key
from schema.message import MessageResp, MessageSend, MessageRefactor, MessagesResp
from crud import message


def get_all_messages(session: Session,
                     *,
                     last_key: str | None = None,
                     limit: int = 100
                     ) -> MessagesResp:
    last_date = get_date_by_key(session, last_key=last_key)
    messages: list[MessageResp] = message.get_all_messages(session, last_date=last_date, limit=limit)
    logger.info(messages[-1])
    res = MessagesResp(
        last_key=messages[-1].id,
        message_resp=messages
    )
    return res


def get_messages_by_user(user_id: int) -> list[MessageResp]:
    pass


def get_message_by_id(message_id: int) -> MessageResp:
    pass


def send_message(body: MessageSend) -> MessageResp:
    pass


def delete_message(message_id: str) -> MessageResp:
    pass


def refactor_message(message_id: str, body: MessageRefactor) -> MessageResp:
    pass
