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
    return {"register_number to dog":dog_data.register_number}

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

def update_user_profile(user_id: int, updated_data: dict): #обновить профиль пользователя
    user = get_user(user_id)
    if user:
        user_data = user.dict()
        user_data.update(updated_data)
        
        updated_user = UserProfile(**user_data)
        if update_user(user_id, updated_user):
            return True
    return False
