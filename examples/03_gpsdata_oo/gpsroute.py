import haversine
import gpspoint


class GPSRoute:

    def __init__(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        counter = 0
        self.gps_points = []
        for line in lines:
            if counter > 1:
                split_line = line.split(',')
                gps_point = gpspoint.GPSPoint(time=split_line[0],
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
