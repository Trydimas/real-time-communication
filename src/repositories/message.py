from sqlalchemy.orm import Session
from schema.message import MessageResp, MessageSend, MessageRefactor, MessagesResp
from crud import message



def check_message(messages: list[MessageResp]):
    for i in messages:
        i.is_checked = True


def get_all_messages(session: Session,
                     *,
                     last_key: str | None = None,
                     limit: int = 100
                     ) -> MessagesResp:
    last_date = message.get_date_by_key(session, last_key=last_key)
    messages = message.get_all_messages(session, last_date=last_date, limit=limit)
    last_key = messages[-1].id if len(messages) else None
    res = MessagesResp(
        last_key=last_key,
        message_resp=messages
    )
    return res


def get_messages_by_user(session: Session,
                         *,
                         user_id: str
                         ) -> MessagesResp:
    return message.get_messages_by_user()


def get_message_by_id(message_id: int) -> MessageResp:
    pass


def send_message(body: MessageSend) -> MessageResp:
    pass


def delete_message(message_id: str) -> MessageResp:
    pass


def refactor_message(message_id: str, body: MessageRefactor) -> MessageResp:
    pass
