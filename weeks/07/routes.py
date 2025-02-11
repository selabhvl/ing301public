from coordinates import Coordinate
from parse import read_file, SHORT_ROUTE
from datetime import datetime

class Route:
    pass

class EndRoute(Route):
    pass 

class RoutePoint(Route):
    
    def __init__(self, geo: Coordinate, ts: datetime, height: float, next: Route):
        self.geo = geo
        self.ts = ts 
        self.height = height
        self.next = next

end = EndRoute()
p1 = RoutePoint(Coordinate(60, 5), datetime(2025, 2, 13, 15, 0), 20, end)
p2 = RoutePoint(Coordinate(61, 4), datetime(2025, 2, 13, 12, 0), 20, end)
# som list
ps = [
    (Coordinate(61, 4), datetime(2025, 2, 13, 12, 0), 20),
    (Coordinate(60, 5), datetime(2025, 2, 13, 15, 0), 20),
      ]        



