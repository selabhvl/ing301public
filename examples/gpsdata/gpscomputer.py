import gpsutils
import haversine

# total distance of the route represented by the GPS points
def total_distance(gps_data: list[tuple[int, float, float, float]]) -> float:
    distance = 0.0

    for i in range(len(gps_data) - 1):
        gps_point1 = gps_data[i]
        gps_point2 = gps_data[i + 1]

        distance = distance + haversine.distance(gps_point1[1], gps_point1[2], gps_point2[1], gps_point2[2])

    return distance


# total elevation gain on the route
def total_elevation(gps_data: list[tuple[int, float, float, float]]) -> float:
    elevation = 0.0

    for i in range(len(gps_data) - 1):
        gps_point1 = gps_data[i]
        gps_point2 = gps_data[i + 1]

        diff = gps_point2[3] - gps_point1[3]

        # sum only if we are going up between two points
        if diff > 0:
            elevation = elevation + diff

    return elevation


# total time of the route from start to finish (first to last point)
def total_time(gps_data: list[tuple[int, float, float, float]]) -> int:
    gps_point_first = gps_data[0]
    gps_point_last = gps_data[len(gps_data) - 1]

    return gps_point_last[0] - gps_point_first[0]


# list with speeds of the individual segments
def segment_speeds(gps_data: list[tuple[int, float, float, float]]) -> list[float]:
    speeds = list()

    for i in range(len(gps_data) - 1):
        gps_point1 = gps_data[i]
        gps_point2 = gps_data[i + 1]

        time = gps_point2[0] - gps_point1[0]

        speed = gpsutils.speed(time, gps_point1[1], gps_point1[2], gps_point2[1], gps_point2[2])

        speeds.append(speed)

    return speeds


# maximum speeds in a segment on the route
def max_speed(gps_data: list[tuple[int, float, float, float]]) -> float:
    speeds = segment_speeds(gps_data)

    max_segment_speed = gpsutils.find_max(speeds)

    return max_segment_speed


# average speed on the complete route
def average_speed(gps_data: list[tuple[int, float, float, float]]) -> float:
    gps_total_time = total_time(gps_data)

    distance = total_distance(gps_data)

    average = ((distance / gps_total_time) * 60 * 60) / 1000

    return average


# kcal burned on a segment
def kcal(weight: float, secs: int, speed: float) -> float:
    # conversion factor m / s to miles per hour
    MS = 2.236936

    speed_mph = speed * MS

    if speed_mph < 10.0:
        met = 4.0
    elif speed_mph < 12.0:
        met = 6.0
    elif speed_mph < 14.0:
        met = 8.0
    elif speed_mph < 16.0:
        met = 10.0
    elif speed_mph < 20.0:
        met = 12.0
    else:
        met = 16.0

    # Energy Expended(kcal) = MET x Body Weight(kg) x Time(h)

    energy_kcal = met * weight * (secs / (60.0 * 60.0))

    return energy_kcal


# total energy as represented by the route
def total_energy(gps_data: list[tuple[int, float, float, float]], weight: float) -> float:
    speeds = segment_speeds(gps_data)

    total_kcal = 0.0

    for i in range(len(speeds) - 1):
        gps_point1 = gps_data[i]
        gps_point2 = gps_data[i + 1]

        time = gps_point2[0] - gps_point1[0]

        energy = kcal(weight, time, speeds[i])

        total_kcal = total_kcal + energy

    return total_kcal


# print out a summary of the key figures
def print_summary(weight: float, gps_data: list[tuple[int, float, float, float]]):
    print("Total Time     : " + gpsutils.print_time(total_time(gps_data)) + " s")
    print("Total distance : {:.2f} km".format(total_distance(gps_data) / 1000.0))
    print("Total elevation: {:.2f} m".format(total_elevation(gps_data)))
    print("Max speed      : {:.2f} km/t".format(max_speed(gps_data)))
    print("Average speed  : {:.2f} km/t".format(average_speed(gps_data)))
    print("Energy         : {:.2f} kcal".format(total_energy(gps_data, weight)))
