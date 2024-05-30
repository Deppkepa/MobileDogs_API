from fastapi import FastAPI
from models import DogProfile, UserProfile, Role
import services
from logger import get_logger

logger=get_logger("main")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info(f"Hello world said")
    return {"message": "Hello World"}


@app.post("/register")
def register_user(user: UserProfile):
    logger.info(f"User {user.user_id} trying to register")
    return services.register_new_user(user)

@app.post("/role_register")
def role_register(user: UserProfile, role: Role):
    return user,role


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

