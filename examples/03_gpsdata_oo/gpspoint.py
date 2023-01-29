from datetime import datetime


class GPSPoint:

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
