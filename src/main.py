from controllers.message import router
from fastapi import FastAPI


app = FastAPI()

app.include_router(router)




if __name__ == "__main__":
    pass