from datetime import datetime
from typing import Optional

class RoutePoint:

    def __init__(self, timestamp: datetime):
        self.timestamp = timestamp
        self.latitude = None
        self.longitude = None
        self.height = None
        self.heart_frequency = None
        self.temperature = None
        self.velocity = None
        self.next = None

    def __repr__(self):
        return f"{self.timestamp} ({self.latitude}, {self.longitude}) {self.height}m"


class AbstractRoute:

    def __init__(self):
        self.totalLength = None
        self.totalHeight = None
        self.averageSpeed = None
        self.maxSpeed = None
        self.usedCalories = None

    def calculateStatistic(self):
        pass


class RouteGroup(AbstractRoute):

    def __init__(self, name: str):
        self.name = name


class RouteIterator:

    def __init__(self, current: Optional[RoutePoint]):
        self.current = current

    def __next__(self):
        result = self.current
        if not result:
            raise StopIteration()
        self.current = result.next
        return result


class Route(AbstractRoute):

    def __init__(self):
        self.first = None
        self.last = None

    def add_point(self, point: RoutePoint):
        if not self.first:
            self.first = point
            self.last = point
        else:
            self.last.next = point
            self.last = point

    def __iter__(self):
        return RouteIterator(self.first)

