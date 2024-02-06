from typing import List
import random as rnd 
from datetime import datetime, timedelta




class RouteGroupComponent:
    
    def count_route(self): # Divide & Conquer, Polymorfisme
        pass


class RouteGroup(RouteGroupComponent):

    def __init__(self, name: str) -> None:
        self.name = name
        self.components : List[RouteGroupComponent] = [] 

    def create_group(self, name: str):
        group = RouteGroup(name)
        self.components.append(group)
        return group
    
    def create_route(self):
        route = Route()
        self.components.append(route)
        return route
    
    def count_route(self):
        sum = 0
        for c in self.components:
            sum += c.count_route()
        return sum

class RouteComponent:
    pass


class RouteIterator:
    
    def __init__(self, current: RouteComponent) -> None:
        self.current = current

    def __next__(self):
        if isinstance(self.current, RoutePoint):
            result = self.current
            self.current = result.next
            return result
        else:
            raise StopIteration
    

class Route(RouteGroupComponent):
    
    def __init__(self) -> None:
        super().__init__()
        placeholder = EmptyRoute()
        self.first = placeholder
        self.last = placeholder

    def __iter__(self):
        return RouteIterator(self.first)

    def add_point(self, ts: str, lat: float, long: float):
        p = RoutePoint(ts, lat, long, self.last, EmptyRoute())
        if isinstance(self.last, EmptyRoute):
            self.first = p 
            self.last = p 
        elif isinstance(self.last, RoutePoint):
            self.last.next = p
            self.last = p 
        return p
        

    def count_route(self):
        return 1





class EmptyRoute(RouteComponent):
    pass


class RoutePoint(RouteComponent):

    # Linked List
    def __init__(self, ts: str, lat: float, long: float, prev: RouteComponent, next: RouteComponent) -> None:
        self.ts = ts 
        self.lat = lat 
        self.long = long
        self.prev = prev 
        self.next = next


class GPSComputer:

    def __init__(self) -> None:
        self.groups = []


    def record_route(self, route: Route):
        file = "gpslogs/short.csv"
        io = open(file, encoding="UTF-8", mode="r")
        lines = io.readlines()
        for l in  lines[2:]:
            line_split = l.split(',')
            route.add_point(line_split[0], float(line_split[1]), float(line_split[2]))
        io.close()


class RouteRecorder:

    def record_route(self, route: Route):
        pass

class CSVReader(RouteRecorder):

    def __init__(self, file: str) -> None:
        super().__init__()
        self.file = file

    def record_route(self, route: Route):
        io = open(self.file, encoding="UTF-8", mode="r")
        lines = io.readlines()
        for l in  lines[2:]:
            line_split = l.split(',')
            route.add_point(line_split[0], float(line_split[1]), float(line_split[2]))
        io.close()

class RandomRecorder(RouteRecorder):
    
    def __init__(self, count: int, start_ts: datetime) -> None:
        super().__init__()
        self.count = count
        self.start_ts = start_ts

    def record_route(self, route: Route):
        for i in range(self.count):
            ts = self.start_ts + timedelta(minutes=i)
            lat = (rnd.random() - 0.5) * 0.001 + 60.3
            long =  (rnd.random() - 0.5) * 0.001 + 5.2
            route.add_point(ts, lat, long)