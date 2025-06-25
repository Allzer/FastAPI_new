from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from database import SessionDep
from src.models.models_main_page.model import BookModel

app = FastAPI()

class BookAddSchema(BaseModel):
    title: str
    author: str

class BookSchema(BookAddSchema):
    id: UUID
    
@app.post('/book')
async def add_book(data: BookSchema, session : SessionDep):
    new_book = BookModel(
        id = data.id,
        title = data.title,
        author = data.author
    )
    session.add(new_book)
    await session.commit() #коммитить только через await
    return {'ok': True}

@app.get('/book')
async def get_book():
    pass

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)