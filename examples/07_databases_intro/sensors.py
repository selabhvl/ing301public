import random
from typing import Tuple
from abc import ABC, abstractmethod


class SensorVisitor(ABC):

    @abstractmethod
    def handle_speedometer(self, speed: float):
        pass

    @abstractmethod
    def handle_temperature(self, temperature: float):
        pass

    @abstractmethod
    def handle_heart_frequency(self, heart_freq: float):
        pass

    @abstractmethod
    def handle_gps(self, gps: Tuple[float, float]):
        pass

    @abstractmethod
    def handle_height(self, height: float):
        pass


class Sensor:

    def __init__(self):
        pass

    def accept(self, visitor: SensorVisitor):
        pass


class GPSSensor(Sensor):

    def __init__(self):
        self.lat = 60.383105
        self.long = 5.309632

    def get_position(self):
        result_lat = self.lat
        result_long = self.long
        self.lat += 0.01 * ((random.random() * 2) - 1)
        self.long += 0.01 * ((random.random() * 2) - 1)
        return result_lat, result_long

    def accept(self, visitor: SensorVisitor):
        visitor.handle_gps(self.get_position())


class Speedometer(Sensor):

    def get_velocity(self) -> float:
        return 20 * random.random()

    def accept(self, visitor: SensorVisitor):
        visitor.handle_speedometer(self.get_velocity())


class TemperatureSensor(Sensor):

    def get_temperatur(self):
        return 16 * random.random()

    def accept(self, visitor: SensorVisitor):
        visitor.handle_temperature(self.get_temperatur())


class HeartFrequencySensor(Sensor):

    def get_frequency(self):
        return 140 * random.random()

    def accept(self, visitor: SensorVisitor):
        visitor.handle_heart_frequency(self.get_frequency())


class HeightSensor(Sensor):

    def __init__(self):
        self.height = 21.0

    def get_height(self):
        result = self.height
        delta = random.random() * 100
        if self.height > 100:
            delta -= 80
        elif self.height > 20:
            delta -= 50
        self.height += round(delta, 1)
        return result

    def accept(self, visitor: SensorVisitor):
        visitor.handle_height(self.get_height())
