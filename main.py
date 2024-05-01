from fastapi import FastAPI
from models import DogProfile, UserProfile, Role
import services

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/register")
def register_user(user: UserProfile):    
    return services.register_new_user(user)

@app.post("/role_register")
def role_register(user: UserProfile, role: Role):
    return user,role


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000,debug=True)

