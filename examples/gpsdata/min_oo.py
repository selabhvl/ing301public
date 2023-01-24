from datetime import datetime
import haversine


class GPSRoute:

    def __init__(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        counter = 0
        self.gps_points = []
        for line in lines:
            if counter >= 1:
                split_line = line.split(',')
                gps_point = GPSPoint(time=split_line[0],
                                     lat=float(split_line[1]),
                                     long=float(split_line[2]),
                                     height=float(split_line[3]))
                self.gps_points.append(gps_point)
            counter += 1

    def find_highest_point(self):
        max_height = 0
        for point in self.gps_points:
            current_height = point.height
            if max_height < current_height:
                max_height = current_height
        return max_height

    def calculate_time(self):
        return self.gps_points[0].time_difference(self.gps_points[-1])

    def calculate_ride_length(self):
        total_distance = 0
        for i in range(0, len(self.gps_points) - 1):
            from_point = self.gps_points[i]
            to_point = self.gps_points[i + 1]
            distance = haversine.distance(from_point.lat, from_point.long, to_point.lat, to_point.long)
            total_distance += distance
        return total_distance


class GPSPoint:
    radius = 6371000

    def __init__(self, time, long, lat, height):
        self.lat = lat
        self.time = time
        self.long = long
        self.height = height

    def time_difference(self, other):
        first_timestamp = datetime.fromisoformat(self.time)
        last_timestamp = datetime.fromisoformat(other.time)
        total_time = last_timestamp - first_timestamp
        return total_time


def main():
    route = GPSRoute("gpslogs/short.csv")

    # Calculating total ride time
    total_time = route.calculate_time()
    print(f"Total Time: {total_time}")

    # Finding highest elevation of the ride
    print(f"Highest Peak: {route.find_highest_point()} masl")

    # Finding total distance of the ride
    total_distance = route.calculate_ride_length()
    total_distance_km = total_distance / 1000.0
    print("Total distance: {:.2f} km".format(total_distance_km))

    print("Average speed: {:.2f} km/h".format(total_distance_km / (total_time.total_seconds() / (60 * 60))))


if __name__ == "__main__":
    main()
