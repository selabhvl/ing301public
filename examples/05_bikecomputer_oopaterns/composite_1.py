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
    

    

class Route(RouteGroupComponent):
    
    def __init__(self) -> None:
        super().__init__()
        self.points = []

    def count_route(self):
        return 1




class RoutePoint:

    def __init__(self, ts: str, lat: float, long: float) -> None:
        self.ts = ts 
        self.lat = lat 
        self.long = long
