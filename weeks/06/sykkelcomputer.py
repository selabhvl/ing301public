from __future__ import  annotations
from datetime import datetime

class Sensor:

    def __init__(self):
        self.last_measurement_timestamp = None

    def measure(self):
        self.last_measurement_timestamp = datetime.now()



class GpsSensor(Sensor):
    pass

class BikeComputer:

    def __init__(self, gps_sensor: GpsSensor, speedometer: Speedometer, temperature_sensor, heart_freq):
        self.gps_sensor = gps_sensor
        self.speedometer = speedometer
        self.temperature_sensor = temperature_sensor
        self.heart_freq = heart_freq



class Speedometer(Sensor):

    def __init__(self, relative_speed: float):
        self.relative_speed = relative_speed

    def do_it(self):
        super().measure()

class TemperatureSensor:

    def __init__(self, temperature: float):
        self.temperature = temperature

    def measure(self):
        pass

class HeartFrequencySensor:
    pass

class GPSPoint:
    pass

class Route:
    pass

class Display:
    pass