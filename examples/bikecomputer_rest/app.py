# https://realpython.com/api-integration-in-python/

# python3 -m pip install flask
# export FLASK_APP=app.py
# flask run

# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

GPSPOINT = "2017-09-08T13:49:50.000Z,60.377625,5.328243,56.2,15.1,158.25,7.297732,0,gps,99.99,99.99,99.99,,,,,98.0,"

@app.get("/gpsdata")
def get_gpsdata():
    return jsonify(GPSPOINT)


@app.post("/gpsdata")
def add_gpsdata():
    pass
