from typing import Dict
from models import DogProfile, UserProfile, Role

database: Dict[int, UserProfile] = {}

def add_user(user: UserProfile):
    database[user.user_id] = user

def get_user(user_id: int):
    return database.get(user_id)

def update_user(user_data: UserProfile):
    if user_data.user_id in database:
        database[user_data.user_id] = user_data
        return True
    else:
        return False
