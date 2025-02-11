from __future__ import annotations

from coordinates import Coordinate
from parse import read_file, SHORT_ROUTE
from datetime import datetime, timedelta


class RouteIterator:

    def __init__(self, current):
        self.current = current

    def has_next(self) -> bool:
        return isinstance(self.current, RoutePoint)
    
    def next(self):
        next_current = self.current.next
        result = self.current
        self.current = next_current
        return result
    
    def __next__(self):
        if self.has_next():
            return next()
        else:
            raise StopIteration()
    

class AggregationStrategy:

    def start_value(self):
        pass

    def aggregate(self, old_aggregate, point_1: RoutePoint, point_2: RoutePoint):
        pass


class TotalDistance(AggregationStrategy):
    
    def start_value(self):
        return 0.0

    def aggregate(self, old_aggregate, point_1, point_2):
        distance = point_1.geo.distance_to(point_2.geo)
        return old_aggregate + distance


class TotalTime(AggregationStrategy):

    def start_value(self):
        return timedelta(seconds=0)
    
    def aggregate(self, old_aggregate, point_1, point_2):
        diff = point_2.ts - point_1.ts
        return old_aggregate + diff
    
class TotalClimb(AggregationStrategy):

    def start_value(self):
        return 0.0
    
    def aggregate(self, old_aggregate, point_1, point_2):
        if point_2.height > point_1.height:
            diff = point_2.height - point_1.height
            return old_aggregate + diff
        else:
            return old_aggregate




class Route:

    def prepend(self, geo: Coordinate, ts: datetime, height: float):
        new_point = RoutePoint(geo, ts, height, self)
        return new_point
    
    def aggregate(self, strategy: AggregationStrategy):
        pass
    
    def __iter__(self):
        return RouteIterator(self)

class EndRoute(Route):

    def aggregate(self, strategy):
        return strategy.start_value() 


class RoutePoint(Route):
    
    def __init__(self, geo: Coordinate, ts: datetime, height: float, next: Route):
        self.geo = geo
        self.ts = ts 
        self.height = height
        self.next = next

    def aggregate(self, strategy):
        if isinstance(self.next, EndRoute):
            return strategy.start_value()
        elif isinstance(self.next, RoutePoint):
            old_aggregate = self.next.aggregate(strategy)
            return strategy.aggregate(old_aggregate, self, self.next)



route = EndRoute()

verdiene = read_file(SHORT_ROUTE)
verdiene.reverse()

for verdi in verdiene:
    route = route.prepend(geo=Coordinate(verdi[1], verdi[2]), ts=verdi[0], height=verdi[3])

distance = route.aggregate(TotalDistance())
time = route.aggregate(TotalTime())
climb = route.aggregate(TotalClimb())

print(f"Distance: {round(distance / 1000, 2)} km")
print(f"Time: {time}")
print(f"Speed: {round(distance / 1000 / (time.total_seconds() / 60 / 60), 2)} km/h")
print(f"Climb: {climb} m")
    

   



