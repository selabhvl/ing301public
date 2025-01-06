from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Person(BaseModel):
    name: str 
    age : int
    is_female: bool | None
    

@app.get("/")
def hello(name: str | None = None):
    """
    Returns a person object
    """
    print(f"Argument was {name}")
    p = Person(name="ole", age=27, is_female=None)
    return p