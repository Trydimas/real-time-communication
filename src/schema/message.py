from pydantic import BaseModel
from models.message import StatusEnum
from datetime import datetime
from schema.user import UserResp


class MessageBase(BaseModel):
    user_id: str
    text: str


class MessageResp(MessageBase):
    id: str
    is_checked: bool
    status: StatusEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MessagesResp(BaseModel):
    last_key: str | None
    message_resp: list[MessageResp]


class MessageRefactor(MessageBase):
    class Config:
        fields = {
            "user_id": {"exclude": True}
        }


class MessageSend(MessageBase):
    pass


class MessgeUser(MessageResp):
    user: UserResp
