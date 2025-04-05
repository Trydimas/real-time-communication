from pydantic import BaseModel
from models.message import StatusEnum
from datetime import datetime
from user import UserResp


class MessageBase(BaseModel):
    user_id: str
    text: str


class MesageResp(MessageBase):
    id: str
    is_checked: bool
    status: StatusEnum
    created_at: datetime
    updated_at: datetime
    user: UserResp


class MessageSend(MessageBase):
    pass


class MessageRefactor(MessageBase):
    class Config:
        fields = {
            "user_id": {"exclude": True}
        }
