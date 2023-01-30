import gpsroute


def main():
    GPS_DATA_FILES = ['short', 'medium', 'long', 'vm']

    GPS_DATA_FILE = GPS_DATA_FILES[3]
    route = gpsroute.GPSRoute("gpslogs/" + GPS_DATA_FILE + ".csv")

    # Calculating total ride time
    total_time = route.calculate_time()
    print(f"Total Time: {total_time}")

    # Finding highest elevation of the ride
    print(f"Highest Peak: {route.find_highest_point()} meter above sea level")

    # Finding total distance of the ride
    total_distance = route.calculate_ride_length()
    total_distance_km = total_distance / 1000.0

    print("Total distance: {:.2f} km".format(total_distance_km))
    print("Average speed: {:.2f} km/h".format(total_distance_km / (total_time.total_seconds() / (60 * 60))))


if __name__ == "__main__":
    main()
