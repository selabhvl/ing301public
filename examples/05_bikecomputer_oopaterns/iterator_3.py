from typing import List

class GPSComputer:

    def __init__(self) -> None:
        self.groups = []



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
