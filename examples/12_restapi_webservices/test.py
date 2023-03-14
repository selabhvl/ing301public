from routes import Routes, Route, GPSPoint

routes = Routes(next_rid=1, routes=list())

route1 = Route(rid=1, gps_points=[])
route2 = Route(rid=2, gps_points=[])

routes.create_route(route1)
routes.create_route(route2)

print(routes)

print(routes.read_route(1))




