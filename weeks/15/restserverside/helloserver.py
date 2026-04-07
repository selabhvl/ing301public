from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):

    content:str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, message: Message):
    return {"item_id": item_id, "message": message}