from haversine import distance


def total_distance(gps_data):
    """
    Calculates the total distance of the route in KM.
    """
    accumulated_distance = 0
    for i in range(len(gps_data)-1):
        accumulated_distance += distance(gps_data[i].lat, gps_data[i].lon, gps_data[i+1].lat, gps_data[i+1].lon)

    return accumulated_distance/1000


# total elevation gain on the route
def total_elevation(gps_data) -> float:
    """
    Calculates the total elevation gain of the route.
    """
    accumulated_elevation = 0
    for i in range(len(gps_data)-1):
        x = gps_data[i+1].elevation - gps_data[i].elevation
        if x > 0:
            accumulated_elevation += x
    return accumulated_elevation


# total time of the route from start to finish (first to last point)
def total_time(gps_data):
    """
    Calculates total time used in record
    """
    firstdatapoint = gps_data[0]
    lastdatapoint = gps_data[-1]
    totaltime = lastdatapoint.time - firstdatapoint.time
    return totaltime


def max_speed(gps_data):
    """
    Calculates maximum speed among the segments of the route in km/t.
    """
    maxspeed = 0
    for i in range(len(gps_data)):
        x = gps_data[i].speed
        if maxspeed < x:
            maxspeed = x
    return maxspeed*3.6


# average speed on the complete route
def average_speed(gps_data):
    """
    Calculates average speed of the complete route.
    """
    tot_time = total_time(gps_data).total_seconds()
    tot_distance = total_distance(gps_data)

    return tot_distance/(tot_time/3600)


# kcal burned on a segment


def print_summary(gps_data):
    """
    Prints a general summary with key figures of the route.
    """
    print("Total Time     : {}  ".format(total_time(gps_data)))
    print("Total distance : {} km".format(total_distance(gps_data)))
    print("Total elevation: {} m".format(total_elevation(gps_data)))
    print("Max speed      : {} km/t".format(max_speed(gps_data)))
    print("Average speed  : {} km/t".format(average_speed(gps_data)))
