# LOCAL
# uvicorn cloudservice:app - -reload

# CLOUD AZURE
# https://portal.azure.com/
# NOTE: Private IP for running web server, External IP from the Arduino
# EXTERNAL IP: 51.105.124.161
# uvicorn --host 10.10.8.5 --port 8080 cloudservice:app

from fastapi import FastAPI, Response, status
from counter import Counter

app = FastAPI()

counters = Counter(red=0, green=0)


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
