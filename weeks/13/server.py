from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def hello():
    return Response(""" 
<!DOCTYPE html>
<html>
<head>
<title>my side</title>
</head>
<body>
<h1>Hi</h1>
<p>How are you</p>
</body>
</html>    
""", media_type="text/html")

@app.get("/weather")
def handle_wather():
    return {'weather': "sunny", "temperature": 6.7}

@app.get("/weather/{location}")
def handle_bergen(location, time = None):
    print(f"Requested weather in {location}")
    return {'weather': "sunny", "temperature": 6.7}

@app.post("/weather/{location}")
def handle_change_weather(location, new_weather: dict):
    print(f"Someone requested the weather in {location} to change to {new_weather}")
    return "OK"
