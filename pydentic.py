from pydantic import BaseModel, EmailStr, Field, ConfigDict
from fastapi import FastAPI

app = FastAPI()

data = {
    "email" : "abc@mail.ru",
    "bio" : None,
    "age" : 12,
}

data_wo_age = {
    "email" : "abc@mail.ru",
    "bio" : None,
    'gender' : 'male',
    'birthday' : '2003'
}

class UserSchema(BaseModel):
    email : EmailStr
    bio : str | None = Field(max_length=100)

    model_config = ConfigDict(extra='forbid')

class UserAgeSchema(UserSchema):
    age : int = Field(ge=0, le=100)

users = []

@app.post('/users')
def create_user(user : UserSchema):
    users.append(user)
    print(users)
    return {'request' : f'Добален User {user}'}

@app.get('/get_users')
def get_users() -> list[UserSchema]:
    return users
