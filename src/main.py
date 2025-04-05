from db import create_tables
from controllers.message import router
from fastapi import FastAPI


app = FastAPI()

app.include_router(router)




if __name__ == "__main__":
    create_tables()