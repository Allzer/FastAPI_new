from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)