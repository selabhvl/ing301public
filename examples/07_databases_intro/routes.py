import operator
from datetime import datetime
from typing import Optional, Callable
import math
from itertools import pairwise, starmap
from functools import reduce
import pickle

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

    def height_difference(self, other):
        return other.height - self.height

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

    def persist(self, location: str):
        fil = open(location, "w", encoding="UTF-8", newline="\n")
        fil.write("timestamp,lat,long,height\n")
        for point in self:
            fil.write(f"{point.timestamp},{point.latitude},{point.longitude},{point.height}\n")
        fil.close()

    def persist_alternative(self, location: str):
        fil = open(location, "wb",)
        pickle.dump(self, fil)
        fil.close()


    def __iter__(self):
        return RouteIterator(self.first)

    def __len__(self):
        if not self.first:
            return 0
        else:
            current = self.first
            result = 1
            while current:
                current = current.next
                result += 1
            return result

    def calculateStatistic(self):
        self.totalLength = round(self.calulate_total_length() / 1000, 2)
        self.totalHeight = round(self.calculate_total_height(), 2)
        self.averageSpeed = round((self.calulate_total_length() / 1000) / (self.calulate_total_time() / 3600), 2)
        self.maxSpeed = round(self.find_average_speed(), 2)

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

    def calculate_total_height(self):
        return reduce(operator.add, [d for d in starmap(RoutePoint.height_difference, pairwise(self)) if d > 0], 0)

    def find_average_speed(self):
        mx = 0
        for p, q in pairwise(self):
            m = p.distance_to(q) / 1000
            t = p.time_difference(q) / 3600
            s = m / t
            if (s > mx):
                mx = s
        return mx





