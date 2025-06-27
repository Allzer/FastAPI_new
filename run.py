from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException, Response
from pydantic import BaseModel
import uvicorn

from sqlalchemy import select
from config import SECRET
from database import SessionDep
from src.models.models_main_page.model import BookModel

from src.main_page.main_page import router as main_page_router


from authx import AuthX, AuthXConfig


app = FastAPI()

app.include_router(main_page_router)


# TOODO Разобраться с JWT
config = AuthXConfig()
config.JWT_SECRET_KEY = SECRET #секретный ключ для генерации jwt
config.JWT_ACCESS_COOKIE_NAME = 'my_token' #Название токена
config.JWT_TOKEN_LOCATION = ['cookies'] #храни токен в куках

# security = AuthX(config=config)

# #Главная страница
# class BookAddSchema(BaseModel):
#     title: str
#     author: str

# class BookSchema(BookAddSchema):
#     id: UUID
    
# @app.post('/book')
# async def add_book(data: BookSchema, session : SessionDep):
#     new_book = BookModel(
#         id = data.id,
#         title = data.title,
#         author = data.author
#     )
#     session.add(new_book)
#     await session.commit() #коммитить только через await
#     return {'ok': True}

# @app.get('/book')
# async def get_book(session : SessionDep):
#     query = select(BookModel)
#     result = await session.execute(query)
#     print(result.all())
#     return result.scalars().all()

# #Auth (Добавить логин пароль в бд и в дальнейшем брать из бд. Обычно пишут свою авторизацию)
# '''В jwt можно передавать данныЕ, но он очень много весит, поэтому нужно думать что передавать, ибо это нагружает систему'''
# class UserLoginSchema(BaseModel):
#     username: str
#     password: str

# @app.post('/login')
# async def login(creads: UserLoginSchema, responce : Response):
#     if creads.username == 'admin' and creads.password == 'admin':
#         token = security.create_access_token(uid='123qweasd')
#         responce.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
#         return {'access_token': token}
#     raise HTTPException(status_code=401, detail='Неверный логин или пароль') #код 401 т.к не прошла аунтефикация

# @app.get('/protected', dependencies=[Depends(security.access_token_required)]) #разобраться с dependencies
# async def login():
#     return {'ok': 'Данные'}

if __name__ == '__main__':
    uvicorn.run('run:app', reload=True)