import math


# earth radius in meters
R = 6371000

def _distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> float:
    """
    Distance between two GPS points in meters as per the haversine formula.

    Reading link:
    https://en.wikipedia.org/wiki/Haversine_formula
    """
    phi_1 = math.radians(latitude1)
    phi_2 = math.radians(latitude2)

    delta_phi = math.radians(latitude2 - latitude1)
    delta_delta = math.radians(longitude2 - longitude1)

    a = _compute_a(phi_1, phi_2, delta_phi, delta_delta)

    c = _compute_c(a)

    d = R * c

    return d


def _compute_c(a):
    return 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def _compute_a(phi_1: float, phi_2: float, delta_phi: float, delta_delta: float) -> float:
    return math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + math.cos(phi_1) * math.cos(phi_2) * (
            math.sin(delta_delta / 2) * math.sin(delta_delta / 2))


class Coordinate:

    __slots__ = ["_latitude", "longitude"]

    def _get_latitude(self):
        return self._latitude
    
    def _set_latitude(self, latitude):
        raise ValueError("coordinates are immutable")

    latitude = property(fget=_get_latitude, fset=_set_latitude)
    
    def __init__(self, latitude: float, longitude: float):
        self._latitude = latitude
        self.longitude = longitude

    

 
    def distance_to(self, other):
        return _distance(self.longitude, self.latitude, other.longitude, other.latitude)

    def __sub__(self, other):
        return self.distance_to(other)
    
    def __repr__(self):
        return f"({self.latitude}, {self.longitude})"
    



