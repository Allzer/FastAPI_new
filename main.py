from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/', tags=['Основные ручки'])
def home():
    return 'Hell world'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)