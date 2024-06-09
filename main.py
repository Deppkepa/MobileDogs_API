from fastapi import FastAPI, Body
from typing import Annotated
from models import DogProfile, UserProfile, Role, Notification, Task
import services
from logger import get_logger

logger=get_logger("main")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info(f"Hello world said")
    return {"message": "Hello World"}

@app.post("/assign_task")
def assign_task_to_user(sender: UserProfile, reciever: UserProfile,task_id: Annotated[int, Body()]):
    return services.assign_task_to_user(sender,reciever,task_id)

@app.post("/get_user_tasks")
def get_user_tasks(user: UserProfile):
    logger.info(f"User {user.user_id} trying to get tasks info")
    return services.get_tasks(user)

@app.post("/register")
def register_user(user: UserProfile):
    logger.info(f"User {user.user_id} trying to register")
    return services.register_new_user(user)
@app.post("/register-dog")
def register_dog(dog: DogProfile):
    logger.info(f"Dog {dog.register_number} trying to register")
    return services.register_new_dog(dog)

@app.post("/info-profile-dog") #ввывод профиля собаки 
def info_profile_dog(register_number: dict):
    logger.info(f"Dog info profile output")
    return services.info_profile_dog(register_number)

@app.post("/info-profile-user") #ввывод профиля собаки
def info_profile_user(user_id: dict):
    logger.info(f"User info profile output")
    return services.info_profile_user(user_id)
@app.post("/create-task") #ввывод профиля собаки
def create_task(task: Task):
    logger.info(f"Request for creating a task.")
    return services.create_task(task)

@app.post("/checkbox-task") #
def checkbox_task(task_id: dict):
    logger.info(f"Request for checkbox a task.")
    return services.checkbox_task(task_id)
@app.post("/notify")
def notify_user(notification: Notification):
    logger.info(f"Trying to notify user {notification.reciever}")
    return services.notify(notification)

@app.post("/attach")
def dog_in_user(request: dict):
    logger.info(f"Trying to assign a dog to user")
    return services.assign_dog_to_user(request)

@app.post("/status-task")
def status_task(task_id: dict):
    logger.info(f"Trying to get status of the task")
    return services.status_task(task_id)

@app.post("/role_update")
def role_update(requast: dict, role: Role):
    return services.role_update(requast, role)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

