from fastapi import APIRouter
from schema.message import MesageResp

router = APIRouter(
    prefix="/messages",
    tags=["message"]
)

#all messages
#messages user's send
#find message by id
#send message
#delete message
#refactor message
#remid about AI, that check message in moment send

@router.get("/")
def get_all_messages() -> list[MesageResp]:
    return