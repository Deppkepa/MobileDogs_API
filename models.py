from datetime import datetime
from pydantic import BaseModel
from typing import List
from enum import Enum

#

#Профиль собаки тут же ошейник
class DogProfile(BaseModel):
    collar_status: str = "OK"
    photo: str
    register_number: int
    name: str
    volunteer_id: List[int] = []
    notes: str = ""
    dog_status: str = "OK"
    tasks: List[int] = []
    location: str = ""

#Список ролей для пользователя
class RoleEnum(str, Enum):
    Admin = 'Admin'
    User = 'User'
    Staff = 'Staff'

#Профиль зарегестрированного пользователя
class UserProfile(BaseModel):
    user_id: int = None
    photo: str = ""
    organization: str = ""
    assigned_dogs: List[int] = []
    last_online: str = ""
    tasks: List[int] = []
    role: RoleEnum
    email: str
    name: str
    password: str
#Роль пользователя
class Role(BaseModel):
    role_name: RoleEnum

#Задача
class Task(BaseModel):
    task_id: int = None
    description: str #описание
    verified: bool = False #выполнена ли задача
    executors: List[int] = [] #исполнители
    deadline: datetime #дедлайн

#Уведомление
class Notification(BaseModel):
    reciever: int
    message: str
