import random
from typing import Tuple
from abc import ABC, abstractmethod

class SensorVisitor(ABC):

    @abstractmethod
    def handleSpeedometer(self, speed: float):
        pass

    @abstractmethod
    def handleTemperature(self, temperature: float):
        pass

    @abstractmethod
    def handleHeartFrequency(self, heart_freq: float):
        pass

    @abstractmethod
    def handleGPS(self, gps: Tuple[float, float]):
        pass


class Sensor:

    def __init__(self):
        pass

    def accept(self, visitor: SensorVisitor):
        pass


class GPSSensor(Sensor):

    def get_position(self):
        return (65.0 * random.random(), 7.0 * random.random())

    def accept(self, visitor: SensorVisitor):
        visitor.handleGPS(self.get_position())


class Speedometer(Sensor):

    def get_velocity(self) -> float:
        return 20 * random.random()

    def accept(self, visitor: SensorVisitor):
        visitor.handleSpeedometer(self.get_velocity())


class TemperatureSensor(Sensor):

    def get_temperatur(self):
        return 16 * random.random()

    def accept(self, visitor: SensorVisitor):
        visitor.handleTemperature(self.get_temperatur())


class HeartFrequencySensor(Sensor):

    def get_frequency(self):
        return 140 * random.random()

    def accept(self, visitor: SensorVisitor):
        visitor.handleHeartFrequency(self.get_frequency())