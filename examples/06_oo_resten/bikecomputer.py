import operator
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from sensors import Sensor, SensorVisitor, GPSSensor, TemperatureSensor, Speedometer
from routes import RoutePoint, Route
from itertools import pairwise, starmap
from functools import reduce

class Display:

    def __init__(self):
        self.speed = 0.0
        self.average_speed = 0.0
        self.total_distance = 0.0
        self.current_distance = 0.0


class CalculateSpeedStrategy:

    def calculate_speed(self) -> float:
        pass


class LookAtSpeedometer(CalculateSpeedStrategy):

    def __init__(self, speedometer: Speedometer):
        self.speedometer = speedometer

    def calculate_speed(self) -> float:
        return self.speedometer.get_velocity()


class CalculateFromGPS(CalculateSpeedStrategy):

    def __init__(self, sensor: GPSSensor):
        self.gsp_sensor = sensor

    def calculate_speed(self) -> float:
        # Beregne tidsforskjell mellom to siste punkt og distance
        # self.current_route.
        pass


class RecordSensorValues(SensorVisitor):

    def __init__(self, to_record_on: RoutePoint):
        self.to_record_on = to_record_on

    def handle_speedometer(self, speed: float):
        self.to_record_on.velocity = speed

    def handle_temperature(self, temperature: float):
        self.to_record_on.temperature = temperature

    def handle_heart_frequency(self, heart_freq: float):
        self.to_record_on.heart_frequency = heart_freq

    def handle_gps(self, gps: Tuple[float, float]):
        self.to_record_on.latitude = gps[0]
        self.to_record_on.longitude = gps[1]

    def handle_height(self, height: float):
        self.to_record_on.height = height


class BikeComputer:

    def __init__(self, display: Display, sensors: List[Sensor]):
        self.display = display
        self.sensors = sensors
        self.current_route = Route()
        self.recorded_routes = []
        for sensor in self.sensors:
            if isinstance(sensor, Speedometer):
                self.speed_strategy = LookAtSpeedometer(sensor)
            elif isinstance(sensor, GPSSensor) and not self.speed_strategy:
                self.speed_strategy = CalculateFromGPS(sensor)

    def simulate_ride(self, ride_duration_seconds: int = 1000, sampling_rate: int = 120):
        clock = timestamp=datetime.utcnow()
        for tick in range(0, ride_duration_seconds, sampling_rate):
            clock += timedelta(sampling_rate)
            p = RoutePoint(timestamp=clock)
            visitor = RecordSensorValues(p)
            for sensor in self.sensors:
                sensor.accept(visitor)
            self.current_route.add_point(p)

    def update_speed(self):
        if self.speed_strategy:
            self.display.speed = self.speed_strategy.calculate_speed()


file = open("../03_gpsdata_oo/gpslogs/short.csv")

route = Route()
skip_count = 0
for line in file.readlines():
    if skip_count > 1:
        splt = line.split(",")
        point = RoutePoint(timestamp=datetime.fromisoformat(splt[0]))
        point.latitude = float(splt[1])
        point.longitude = float(splt[2])
        point.height = float(splt[3])
        route.add_point(point)
    skip_count += 1

file.close()

print("Total distance and time:")

# Home Made aggregation
print(f"{route.calulate_total_length()} m")
print(f"{route.calulate_total_time()} s")

# Library aggregation
print(f"{reduce(operator.add, starmap(RoutePoint.distance_to, pairwise(route)), 0)} m")
print(f"{reduce(operator.add, starmap(RoutePoint.time_difference, pairwise(route)), 0)} s")


def diffs_on(p1: RoutePoint, p2: RoutePoint):
    print(f"time {(p1.timestamp - p2.timestamp).total_seconds()}")


for p in pairwise(route):
    diffs_on(p[0], p[1])
