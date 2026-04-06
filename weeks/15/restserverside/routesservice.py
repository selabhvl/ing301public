
# Install FastAPI framework
# pip3 install "fastapi[all]"
# https://fastapi.tiangolo.com/tutorial/

# Running the REST services in the uvicorn web server
# uvicorn main:app --reload

import uvicorn

from fastapi import FastAPI, Response, status, HTTPException

from routes import Routes, Route, GPSPoint

app = FastAPI()
routes = Routes(next_rid=1, routes={})


@app.get("/")
def root():
    return {"message": "Welcome to the bike computer REST API - Powered by FastAPI"}


@app.get("/route/")
def read_routes():
    return routes.routes


@app.get("/route/{rid}")
def read_route(rid: int):
    route = routes.read_route(rid)
    if route:
        return route
    else:
        raise HTTPException(status_code=404, detail="Route not found")


@app.post("/route/", status_code=201)
def create_route(route: Route):
    added_route = routes.create_route(route)
    return added_route


@app.put("/route/{rid}")
def update_route(rid: int, route: Route):
    updated_route = routes.update_route(rid, route)
    if updated_route:
        return updated_route
    else:
        raise HTTPException(status_code=404, detail="Route not found")


@app.delete("/route/{rid}")
def delete_route(rid: int, response: Response):
    route = routes.delete_route(rid)
    if route:
        return route
    else:
        raise HTTPException(status_code=404, detail="Route not found")


@app.get("/route/{rid}/gpspoint")
def read_gps_points(rid: int):
    gps_points = routes.read_gpspoints(rid)

    if gps_points is not None:
        return gps_points
    else:
        raise HTTPException(status_code=404, detail="Route not found")


@app.get("/route/{rid}/gpspoint/{pid}")
def read_gps_point(rid: int, pid: int):

    gps_point = routes.read_gpspoint(rid, pid)

    if gps_point:
        return gps_point
    else:
        raise HTTPException(status_code=404, detail="Point not found")


@app.post("/route/{rid}/gpspoint", status_code=201)
def create_gps_point(rid: int, gps_point: GPSPoint):
    added_gps_point = routes.create_gpspoint(rid, gps_point)
    return added_gps_point


@app.put("/route/{rid}/gpspoint/{pid}")
def update_point(rid: int, pid: int, gps_point: GPSPoint):
    gps_point_result  = routes.update_gps_point(rid, pid, gps_point)
    if gps_point_result:
        return gps_point_result
    else:
        raise HTTPException(status_code=404, detail="Point not found")


@app.delete("/route/{rid}/gpspoint/{pid}")
def delete_gps_point(rid: int, pid: int):
    gps_point = routes.delete_gps_point(rid, pid)

    if gps_point:
        return gps_point
    else:
        raise HTTPException(status_code=404, detail="Point not found")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
