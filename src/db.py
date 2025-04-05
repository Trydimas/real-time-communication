from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(
    settings.DB_URL,
    echo=True
)

factory_session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)



class Base(DeclarativeBase):
    __abstract__ = True

    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, "__tablename__"):
            cls.__tablename__ = cls.__name__.lower() + "s"
        super().__init_subclass__(**kwargs)
