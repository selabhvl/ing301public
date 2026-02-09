import math


# constant: earth radius in meters
R = 6371000

# Hjelpfunksjon for å beregne avstand mellom to koordinater i meter
def distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> float:
    """
    Distance between two GPS points in meters as per the haversine formula.

    Reading link:
    https://en.wikipedia.org/wiki/Haversine_formula
    """
    phi_1 = math.radians(latitude1)
    phi_2 = math.radians(latitude2)

    delta_phi = math.radians(latitude2 - latitude1)
    delta_delta = math.radians(longitude2 - longitude1)

    a = math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + math.cos(phi_1) * math.cos(phi_2) * (
            math.sin(delta_delta / 2) * math.sin(delta_delta / 2))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = R * c

    return d