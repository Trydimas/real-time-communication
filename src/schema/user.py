from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    email: str | None


class UserResp(BaseUser):
    id: str


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser):
    pass
