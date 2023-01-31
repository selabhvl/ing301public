from datetime import datetime
from typing import List


class Sensor:

    def __init__(self):
        pass


class BikeComputer:
    pass


class Display:
    pass


class GPSPoint:

    def __init__(self, timestamp: datetime, latitude: float, longitude: float, height: float):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.height = height


class Route:

    def __init__(self, gps_points):
        self.totalLength = None
        self.totalHeight = None
        self.averageSpeed = None
        self.maxSpeed = None
        self.usedCalories = None
        self.first = gps_points[0]
        self.last = gps_points[-1]
        self.points = gps_points

    def calculateStatistic(self):
        pass


class GPSSensor(Sensor):
    pass


class Speedometer(Sensor):
    pass


class TemperatureSensor(Sensor):
    pass


class HeartFrequencySensor(Sensor):
    pass


p = GPSPoint(datetime(2023, 1, 24, 12, 23), 2.3455, 31.88723, "10.5")
print(p.height)

s = GPSSensor()
print(s.x)
