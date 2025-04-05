from pydantic import BaseModel
from models.message import StatusEnum
from datetime import datetime
from user import UserResp


class MessageBase(BaseModel):
    user_id: int
    text: str


class MesageResp(MessageBase):
    id: int
    is_checked: bool
    status: StatusEnum
    created_at: datetime
    updated_at: datetime
    user: UserResp

class MessageCreate(MessageBase):
    pass