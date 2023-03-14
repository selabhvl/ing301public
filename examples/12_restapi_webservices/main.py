# Install FastAPI framework
# pip3 install "fastapi[all]"
# https://fastapi.tiangolo.com/tutorial/

from fastapi import FastAPI, Response, status

from routes import Routes, Route, GPSPoint

app = FastAPI()
routes = Routes(next_rid=1, routes= list())

# GET /route/ - all routes in json (could consider also links in case of html
# GET /route/{tid} - retrieve the given route id
# POST /route/ - create a new route with provided GPS points
# PUT /route/{rid} - update a specific route with GPS point list
# DELETE /route/{rid} - delete route with teh given route id

# GET /route/{rid}/gpspoint - all GPS points in the given route
# GET /route/{rid}/gpspoint/{pid}
# PUT /route/{rid}/gpspoint/{pid} - update gps point
# POST /route/{rid}/gpspoint/ - add gps point to route
# DELETE /route/{rid}/gpspoint/{pid} - delete gps point from route


@app.get("/")
async def root():
    return {"message": "Welcome to the bike computer REST API - Powered by FastAPI"}


@app.get("/route/")
async def read_routes():
    return routes.routes


@app.get("/route/{rid}")
async def read_route(rid: int, response: Response):
    route = routes.read_route(rid)
    if route:
        return route
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None


@app.put("/route/{rid}")
async def update_route(rid: int, route: Route, response: Response):
    updated_route = routes.update_route(rid, route)
    if updated_route:
        return updated_route
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None


@app.post("/route/", status_code=201)
async def create_route(route: Route):
    added_route = routes.create_route(route)
    return added_route


@app.delete("/route/{rid}")
async def delete_route(rid: int, response: Response):
    route = routes.delete_route(rid)
    if route:
        return route
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None


# GET /route/{rid}/gpspoint - all GPS points in the given route
@app.get("/route/{rid}/gpspoint")
async def read_gps_points(rid: int, response: Response):
    gps_points = routes.read_gpspoints(rid)
    if gps_points:
        return gps_points
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None


# GET /route/{rid}/gpspoint/{pid}
@app.get("/route/{rid}/gpspoint/{pid}")
async def read_gps_point(rid: int, pid: int, response: Response):
    print(f"rid: {rid} pid: {pid}")
    gps_point = routes.read_gpspoint(rid, pid)
    if gps_point:
        return gps_point
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None


# PUT /route/{rid}/gpspoint/{pid} - update gps point
@app.put("/route/{rid}/gpspoint/{pid}")
async def update_point(rid: int, pid: int, gps_point: GPSPoint, response: Response):
    gps_point = routes.update_gps_point(rid, pid, gps_point)
    if gps_point:
        return gps_point
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None


# POST /route/{rid}/gpspoint/ - add gps point to route
@app.post("/route/{rid}/gpspoint", status_code=201)
async def create_gps_point(rid: int, gps_point: GPSPoint):
    added_gps_point = routes.create_gpspoint(rid, gps_point)
    return added_gps_point


# DELETE /route/{rid}/gpspoint/{pid} - delete gps point from route
@app.delete("/route/{rid}/gpspoint/{pid}")
async def delete_gps_point(rid: int, pid: int, response: Response):
    gps_point = routes.delete_gps_point(rid, pid)
    if gps_point:
        return gps_point
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

    return None
