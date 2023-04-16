
# uvicorn cloudservice:app - -reload

from fastapi import FastAPI, Response, status
from counter import Counter

app = FastAPI()

counters = Counter(red=0,green=0)

@app.get("/")
def root():
    return {"message": "Welcome to Counter Cloud REST API - Powered by FastAPI"}

@app.get("/counters")
def get_counters():
    return counters


@app.put("/counters")
def update_counters(updated_counters: Counter):

    counters.red = updated_counters.red
    counters.green = updated_counters.green

    return counters
