from typing import Dict
from models import DogProfile, UserProfile, Role, Task
from logger import get_logger
logger=get_logger("database")

#База данных. Словарь, в котором хранятся пользователи в формате JSON UserProfile
database: Dict[int, UserProfile] = {}

#База данных. Словарь, в котором хранятся задачи в формате JSON Task
Tasks_database: Dict[int, Task] = {}

#База данных. Словарь, в котором хранятся ошейники в формате Json DogProfile
Collar_database: Dict[int, DogProfile] = {}

def assign_task_to_user(sender: int, reciever: int,task_id:int):
    logger.info(f"Assigning task {task_id} to user {reciever}")
    database[reciever].tasks.append(task_id)
    Tasks_database[task_id].executors.append(reciever)
    return {"message":f"Task {task_id} was successfully assigned to user {reciever}"}
 

def get_tasks(user: UserProfile):
    logger.info(f"Getting tasks for user with id: {user.user_id}")
    tasks=[]
    for task in user.tasks:
        tasks.append(Tasks_database[task])
    return tasks

def add_user(user: UserProfile):
    logger.info(f"Adding user {user.user_id} to database")
    database[user.user_id] = user

def get_user(user_id: int):
    logger.info(f"Get_user for user_id: {user_id}")
    return database.get(user_id)

def update_user(user_data: UserProfile):
    if user_data.user_id in database:
        database[user_data.user_id] = user_data
        return True
    else:
        return False
def add_dog(dog: DogProfile):
    logger.info(f"Adding dog {dog.register_number} to Collar_database")
    Collar_database[dog.register_number] = dog

def add_task(task: Task):
    logger.info(f"Adding dog {task.task_id} to Collar_database")
    Tasks_database[task.task_id] = task

def assign_dog(user_id: int, dog_id:int):
    logger.info(f"Adding dog with id {dog_id} to user {user_id}")
    database[user_id].assigned_dogs.append(dog_id)

def task_verified(task_id):
    if (Tasks_database[task_id].verified == True):
        Tasks_database[task_id].verified = False
    else:
        Tasks_database[task_id].verified = True
