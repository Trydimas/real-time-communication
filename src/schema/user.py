from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    email: str | None


class UserResp(BaseUser):
    id: str

    class Config:
        from_attributes = True

class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser):
    pass
