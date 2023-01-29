import haversine

# print seconds in hh:mm:ss format
def print_time(secs: int) -> str:

    hh = secs // 3600
    mm = (secs % 3600) // 60
    ss = (secs % 3600) % 60

    return str(hh)+":"+str(mm)+":"+str(ss)


def find_max(numbers: list[float]) -> float:

    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number


def find_min(numbers: list[float]) -> float:

    min_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number

    return min_number

# distance between two GPS points as per the haversine formula


# average speed between two GPS points
def speed(secs: int, latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> float:
    # m / s
    speed_ms = haversine.distance(latitude1, longitude1, latitude2, longitude2) / secs

    # km / t
    speed_kmh = (speed_ms * 60 * 60) / 1000

    return speed_kmh
