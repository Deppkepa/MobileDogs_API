from pydantic import BaseModel
from typing import List
from enum import Enum

#

#Профиль собаки
class DogProfile(BaseModel):
    collar_status: str
    photo: str
    collar_id: int
    name: str
    volunteer_name: str
    notes: str
    dog_status: str
    tasks: List[int]
    location: str

#Список ролей для пользователя
class RoleEnum(str, Enum):
    Admin = 'Admin'
    User = 'User'
    Staff = 'Staff'

#Профиль зарегестрированного пользователя
class UserProfile(BaseModel):
    user_id: int = 10
    photo: str = "not"
    organization: str = "not"
    assigned_dogs: List[int] = None
    last_online: str = "off"
    tasks: List[int] = None
    role: RoleEnum = "User"
    email: str
    name: str
    password: str
#

#Роль пользователя
class Role(BaseModel):
    role_name: RoleEnum

class Task(BaseModel):
    task_id: int
    description: str
    verified: bool
    executors: List[int]