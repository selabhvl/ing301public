
from pydantic import BaseModel


class GPSPoint(BaseModel):

    lat: float
    long: float
    height: float


class Route(BaseModel):

    rid: int | None = None
    gps_points: list[GPSPoint]

    def get_point(self, pid: int):
        return self.find_point[pid]

    def add_point(self, gps_point: GPSPoint) -> GPSPoint:
        self.gps_points.append(gps_point)
        return gps_point

    def delete_point(self, pid: int):
        del self.gps_points[pid]


class Routes(BaseModel):

    next_rid: int
    routes: dict[int, Route]

    def get_next_rid(self):
        rid = self.next_rid
        self.next_rid += 1
        return rid

    def read_route(self, rid: int):
        return self.routes.get(rid)

    def create_route(self, route: Route) -> Route:
        route.rid = self.get_next_rid()
        self.routes[route.rid] = route
        return route

    def update_route(self, rid, route: Route) -> Route:
        update_route = self.routes.get(rid)
        if update_route:
            update_route.gps_points = route.gps_points
            return self.routes.get(rid)
        else:
            return None

    def delete_route(self, rid: int):
        route = self.routes.pop(rid)
        return route

    def read_gpspoints(self, rid: int):
        route = self.routes.get(rid)

        if route:
            return route.gps_points

        return None

    def read_gpspoint(self, rid: int, pid: int):
        route = self.routes.get(rid)

        if route:
            gps_points = route.gps_points
            print(f"pid: {pid} {len(gps_points)}")
            if pid < len(gps_points):
                return gps_points[pid]

        return None

    def update_gps_point(self, rid: int, pid: int, gps_point: GPSPoint):
        route = self.routes.get(rid)

        if route:
            gps_points = route.gps_points
            if pid < len(gps_points):
                gps_points[pid] = gps_point
                return gps_points[pid]

        return None

    def create_gpspoint(self, rid: int, gps_point: GPSPoint):
        route = self.routes.get(rid)

        if route:
            gps_points = route.gps_points
            gps_points.append(gps_point)
            return gps_points[-1]

        return None

    def delete_gps_point(self, rid: int, pid: int):
        route = self.routes.get(rid)

        if route:
            gps_points = route.gps_points

            if pid < len(gps_points):
                gps_point = gps_points[pid]
                gps_points.pop(pid)

                return gps_point

        return None
