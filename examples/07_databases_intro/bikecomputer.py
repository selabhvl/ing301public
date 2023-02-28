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

    def __init__(self, sensors: List[Sensor]):
        self.display = Display()
        self.sensors = sensors
        self.current_route = Route()
        self.speed_strategy = None
        self.recorded_routes = []
        for sensor in self.sensors:
            if isinstance(sensor, Speedometer):
                self.speed_strategy = LookAtSpeedometer(sensor)
            elif isinstance(sensor, GPSSensor) and not self.speed_strategy:
                self.speed_strategy = CalculateFromGPS(sensor)

    def simulate_ride(self, ride_duration_seconds: int = 1000, sampling_rate: int = 120):
        clock = datetime.utcnow()
        for tick in range(0, ride_duration_seconds, sampling_rate):
            clock = clock + timedelta(seconds=sampling_rate)
            p = RoutePoint(timestamp=clock)
            visitor = RecordSensorValues(p)
            for sensor in self.sensors:
                sensor.accept(visitor)
            self.current_route.add_point(p)
        self.recorded_routes.append(self.current_route)
        self.current_route = Route()

    def update_speed(self):
        if self.speed_strategy:
            self.display.speed = self.speed_strategy.calculate_speed()


