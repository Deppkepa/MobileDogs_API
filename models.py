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
    tasks: List[str]
    location: str

#Список ролей для пользователя
class RoleEnum(str, Enum):
    Admin = 'Admin'
    User = 'User'
    Staff = 'Staff'

#Профиль зарегестрированного пользователя
class UserProfile(BaseModel):
    user_id: int
    photo: str
    organization: str
    assigned_dogs: List[int]
    last_online: str
    tasks: List[str]
    role: RoleEnum
    email: str
    name: str
    password: str

#Роль пользователя
class Role(BaseModel):
    role_name: RoleEnum
