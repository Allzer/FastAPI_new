from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Асинхронность в Python',
        'author': 'Игнат'
    },
    {
        'id': 2,
        'title': 'Backend разработка в Python',
        'author': 'Артём'
    }
]

@app.get('/', tags=['Основные ручки'], summary='Главная страница')
def home():
    return 'Hell world'

@app.get('/books', tags=['Книги'], summary='Получить список книг')
def get_books():
    return books

@app.get('/books/{id}', tags=['Книги'], summary='Получить книгу по Id')
def get_books_on_id(id : int):
    try:
        return books[id]
    except Exception as e:
        raise HTTPException(status_code=404, detail='Книга не найдена')


class Book(BaseModel):
    title : str
    author : str

@app.post('/books', tags=['Книги'])
def add_books(book : Book):
    try:
        books.append(
            {
                'id' : len(books) + 1,
                'title' : book.title,
                'author' : book.author
            }
        )
        return {'request' : 'Книга добалена'}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Книга не добавлена')

        

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)