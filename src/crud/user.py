from schema.user import UserResp
from models.user import User
from models.message import Message
from sqlalchemy.orm import Session


def get_user_by_id(session: Session,
                   *,
                   user_id: str
                   ) -> type[User]:
    user = session.get(User, user_id)
    return user
