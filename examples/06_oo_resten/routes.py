from datetime import datetime
from typing import Optional, Callable
import math



def _compute_c(a):
    return 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def _compute_a(phi_1: float, phi_2: float, delta_phi: float, delta_delta: float) -> float:
    return math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + math.cos(phi_1) * math.cos(phi_2) * (
            math.sin(delta_delta / 2) * math.sin(delta_delta / 2))


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

    def distance_to(self, other):
        """
            Distance between two GPS points in meters as per the haversine formula.

            Reading link:
            https://en.wikipedia.org/wiki/Haversine_formula
            """

        # earth radius in meters
        R = 6371000

        phi_1 = math.radians(self.latitude)
        phi_2 = math.radians(other.latitude)

        delta_phi = math.radians(other.latitude - self.latitude)
        delta_delta = math.radians(other.longitude - self.longitude)

        a = _compute_a(phi_1, phi_2, delta_phi, delta_delta)

        c = _compute_c(a)

        d = R * c

        return d

    def time_difference(self, other):
        diff = other.timestamp - self.timestamp
        return diff.total_seconds()

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


    def calculateStatistic(self):
        self.totalLength = self.calulate_total_length()


    def aggregate(self, operation: Callable[[RoutePoint, RoutePoint], float]):
        if not self.first:
            return 0
        last_point = self.first
        next_point = self.first.next
        total_time = 0
        while next_point:
            total_time += operation(last_point, next_point)
            last_point, next_point = next_point, next_point.next
        return total_time




    def calulate_total_time(self):
        return self.aggregate(RoutePoint.time_difference)


    def calulate_total_length(self):
        return self.aggregate(RoutePoint.distance_to)





