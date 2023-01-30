from datetime import datetime
import haversine


class GPSPoint:

    def __init__(self, time, long, lat, height):
        self.lat = lat
        self.time = time
        self.long = long
        self.height = height

    def time_difference(self, other):
        first_timestamp = datetime.fromisoformat(self.time[:-1])
        last_timestamp = datetime.fromisoformat(other.time[:-1])
        total_time = last_timestamp - first_timestamp
        return total_time

    def distance(self, other):
        return haversine.distance(self.lat, self.long, other.lat, other.long)
