from fastapi import APIRouter
from schema.message import MesageResp, MessageSend, MessageRefactor
from repositories import message

router = APIRouter(
    prefix="/messages",
    tags=["message"]
)


# TODO AI, that check message in moment send

@router.get("/")
def get_all_messages() -> list[MesageResp]:
    return message.get_all_messages()


@router.get("/user/{user_id}")
def get_messages_by_user(user_id: int) -> list[MesageResp]:
    return message.get_messages_by_user(user_id)


@router.get("/{message_id}")
def get_message_by_id(message_id: str) -> MesageResp:
    return message.get_message_by_id(message_id)


@router.post("/")
def send_message(body: MessageSend) -> MesageResp:
    return message.send_message(body)


@router.delete("/{message_id}")
def delete_message(message_id: str) -> MesageResp:
    return message.delete_message(message_id)


@router.put("/{message_id}")
def refactor_message(message_id: str, body: MessageRefactor) -> MesageResp:
    return message.refactor_message(message_id, body)
