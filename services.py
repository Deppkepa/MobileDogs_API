import database
from models import DogProfile, UserProfile, Role, Notification, Task
from logger import get_logger

logger=get_logger("services")
def generate_unique_id():
    id = 0
    if len(database.database) == 0:
        return id
    for i in range(len(database.database)):
        if database.database[i].user_id < id:
            return id
        id += 1
    return id

def generate_unique_id_task():
    id = 0
    if len(database.Tasks_database) == 0:
        return id
    for i in range(len(database.Tasks_database)):
        if database.Tasks_database[i].task_id < id:
            return id
        id += 1
    return id
def register_new_user(user_data: UserProfile):
    if user_data.user_id == None:
        user_data.user_id = generate_unique_id()
    if (user_data.user_id in database.database):
        logger.error(f"User with id: {user_data.user_id} already exists")
        return f"User with id: {user_data.user_id} already exists"
    else:
        for i in database.database:
            if database.database[i].email==user_data.email:
                logger.error(f"Email {user_data.email} is already taken")
                return f"Email {user_data.email} is already taken"

    database.add_user(user_data)
    logger.info(f"User {user_data.user_id} successfully registered")
    return {"user_id":user_data.user_id}

def register_new_dog(dog_data: DogProfile):
    if (dog_data.register_number in database.Collar_database):
        logger.error(f"Dog with id: {dog_data.register_number} already exists")
        return f"Dog with id: {dog_data.register_number} already exists"
    database.add_dog(dog_data)
    logger.info(f"Dog {dog_data.register_number} successfully registered")
    return {"register_number to dog": dog_data.register_number}

def info_profile_dog(register_number: dict):
    for key in register_number:
        if key != "register_number":
            logger.error(f"Key '{key}' does not fit. You need to use 'register_number' as a key")
            return f"Key '{key}' does not fit."
    logger.info(f"Profile dog with number collar {register_number['register_number']} request successfully")
    return {f"Profile dog with number collar": database.Collar_database[int(register_number['register_number'])]}

def info_profile_user(user_id: dict):
    for key in user_id:
        if key != "user_id":
            logger.error(f"Key '{key}' does not fit. You need to use 'user_id' as a key")
            return f"Key '{key}' does not fit."
    if not(user_id['user_id'] in database.database):
        logger.error(f"User with id {user_id['user_id']} is not registered")
        return {"message":f"User with id {user_id['user_id']} is not registered"}
    logger.info(f"Profile user with id {user_id} request successfully")
    return {f"Profile user with id": database.database[user_id['user_id']]}
def notify(note: Notification): #3 запрос уведомления
    if not(note.reciever in database.database):
        logger.error(f"User with id: {note.reciever} is not registered")
        return False
    else:
        logger.info(f"Sending message {note.message} to user with id: {note.reciever}")
        return True
   

def assign_dog_to_user(request: dict): # привязать собаку к пользователю
    if "user_id" in request and type(request["user_id"]) is int:
        user_id = request["user_id"]
        if "register_number" in request and type(request["register_number"]) is int:
            dog_id = request["register_number"]
        else:
            return False
    else:
        return False
    index = -1
    for i in range(len(database.database)):
        if database.database[i].user_id == user_id:
            index = i
    if index == -1:
        logger.error(f"User with id: {user_id} does not exists")
        return False
    if not(dog_id in database.Collar_database):
        logger.error(f"Dog with collar number {dog_id} does not exists")
        return False
    for y in database.database[index].assigned_dogs:
        if dog_id == y:
            logger.error(f"Dog with id: {dog_id} is already assigned to user {user_id}.")
            return False
    database.assign_dog(user_id,dog_id)
    logger.info(f"Dog {dog_id} successfully assigned to user {user_id}")
    return True
def create_task(task: Task):
    if task.task_id == None:
        task.task_id = generate_unique_id_task()
    if (task.task_id in database.Tasks_database):
        logger.error(f"Task with id: {task.task_id} already exists")
        return f"Task with id: {task.task_id} already exists"
    database.add_task(task)
    logger.info(f"Task {task.task_id} successfully registered")
    return {"task_id": task.task_id}

def checkbox_task(task_id: dict):
    for key in task_id:
        if key != "task_id":
            logger.error(f"Key '{key}' does not fit. You need to use 'task_id' as a key")
            return f"Key '{key}' does not fit."
    database.task_verified(task_id['task_id'])
    if database.Tasks_database[task_id['task_id']].verified == True:
        logger.info(f"The task with id {task_id['task_id']} is now verified")
        return "The task is now verified"
    else:
        logger.info(f"The {task_id['task_id']} task is no longer verified")
        return "The task is no longer verified"

def role_update(requast: dict, role: Role):
    return {requast, role}
def update_user_profile(user_id: int, updated_data: dict): #обновить профиль пользователя
    user = get_user(user_id)
    if user:
        user_data = user.dict()
        user_data.update(updated_data)
        
        updated_user = UserProfile(**user_data)
        if update_user(user_id, updated_user):
            return True
    return False

def status_task(task_id: dict):
    for key in task_id:
        if key != "task_id":
            logger.error(f"Key '{key}' does not fit. You need to use 'task_id' as a key")
            return f"Key '{key}' does not fit."
    logger.info(f"Status task with id {task_id['task_id']} request successfully")
    return {f"Status task with id": database.Tasks_database[task_id['task_id']].verified}

def get_tasks(user: UserProfile):
    if not(user.user_id in database.database):
        logger.error(f"User with id: {user.user_id} is not registered")
        return {"message":"User is not registered"}
    for task in user.tasks:
        if not(task in database.Tasks_database):
            logger.error(f"Task with id: {task} does not exist")
            return {"message":f"Task with id: {task} does not exist"}
    return database.get_tasks(database.database[user.user_id])

def assign_task_to_user(sender: UserProfile, reciever: UserProfile,task_id:int):
    if not(sender.user_id in database.database):
        logger.error(f"User with id: {sender.user_id} is not registered")
        return {"message":"User is not registered"}
    else:
        sender=database.database[sender.user_id]
    if not(reciever.user_id in database.database):
        logger.error(f"User with id: {reciever.user_id} is not registered")
        return {"message":"User is not registered"}
    else:
        reciever=database.database[reciever.user_id]
    if not(task_id in database.Tasks_database):
        logger.error(f"Task with id: {task_id} does not exist")
        return {"message":f"Task {task_id} does not exist"}
    
    if sender.role!="Admin":
        logger.error(f"User {sender.user_id} does not have permission to assign a task")
        return {"message":f"User {sender.user_id} does not have permission to assign a task"}
    if task_id in reciever.tasks:
        logger.error(f"User {reciever.user_id} is already assigned to task {task_id}")
        return {"message":f"User {reciever.user_id} is already assigned to task {task_id}"}
    
    return database.assign_task_to_user(sender.user_id,reciever.user_id,task_id)

def give_role_to_user(sender: UserProfile,role: Role,user_id: int):
    if not(sender.user_id in database.database):
        logger.error(f"User with id: {sender.user_id} is not registered")
        return {"message":"User is not registered"}
    else:
        sender=database.database[sender.user_id]
    if not(user_id in database.database):
        logger.error(f"User with id: {user_id} is not registered")
        return {"message":"User is not registered"}
    if sender.role!="Admin":
        logger.error(f"User with id: {sender.user_id} is not an Admin")
        return {"message":f"User with id: {sender.user_id} is not an Admin"}
    return database.give_role_to_user(sender,role,user_id)
        
