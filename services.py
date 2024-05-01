import database
from models import DogProfile, UserProfile, Role

# Пример бизнес-логики приложения
def register_new_user(user_data: UserProfile):
    # Проверка уникальности email и другие проверки
    # Если все проверки пройдены, то регистрируем нового пользователя
    
    if (user_data.user_id in database.database):
        return "User already exists"
    else:
        for i in database.database:
            if database.database[i].email==user_data.email:
                return "Email is already taken"
    database.add_user(user_data)
    return f"User {user_data.name} successfully registered"
    

def assign_dog_to_user(user_id: int, dog_id: int):
    user = database.get_user(user_id)
    if user:
        if dog_id not in user.assigned_dogs:
            user.assigned_dogs.append(dog_id)
            update_user(user)
            return True
    return False

def update_user_profile(user_id: int, updated_data: dict):
    user = get_user(user_id)
    if user:
        user_data = user.dict()
        user_data.update(updated_data)
        
        updated_user = UserProfile(**user_data)
        if update_user(user_id, updated_user):
            return True
    return False
