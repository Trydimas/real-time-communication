from schema.user import UserResp
from models.user import User
from models.message import Message
from sqlalchemy.orm import Session


def get_user_by_id(session: Session,
                   *,
                   user_id: str
                   ) -> UserResp:
    pass
