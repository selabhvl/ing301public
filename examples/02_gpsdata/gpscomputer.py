def total_distance(gps_data):
    """
    Calculates the total distance of the route.
    """
    return NotImplemented


# total elevation gain on the route
def total_elevation(gps_data) -> float:
    """
        Calculates the total elevation gain of the route.
        """
    return NotImplemented


# total time of the route from start to finish (first to last point)
def total_time(gps_data):
    """
    Calculates the total time of the route from start to finish.
    """
    return NotImplemented


def max_speed(gps_data):
    """
    Calculates maximum speed among the segments of the route.
    """
    return NotImplemented


# average speed on the complete route
def average_speed(gps_data: list[tuple[int, float, float, float]]) -> float:
    """
    Calculates average speed of the complete route.
    """
    return NotImplemented


# kcal burned on a segment


def print_summary(gps_data: list[tuple[int, float, float, float]]):
    """
    Prints a general summary with key figures of the route.
    """
    print("Total Time     : {} s ".format(total_time(gps_data)))
    print("Total distance : {} km".format(total_distance(gps_data)))
    print("Total elevation: {} m".format(total_elevation(gps_data)))
    print("Max speed      : {} km/t".format(max_speed(gps_data)))
    print("Average speed  : {} km/t".format(average_speed(gps_data)))
