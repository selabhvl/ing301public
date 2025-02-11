from datetime import datetime
from coordinates import Coordinate
import random



class Sensor:

    def __init__(self):
        self.last_measurement_timestamp = None

    def measure(self):
        self.last_measurement_timestamp = datetime.now()


class GpsSensor(Sensor):

    def measure(self):
        super().measure()
        # random location stored as Coordinate
        self.last_measurement = Coordinate(random.random() * 60, random.random() * 5)

    def __repr__(self):
        return f"{self.last_measurement_timestamp.isoformat()}: ({self.last_measurement.latitude}, {self.last_measurement.longitude})"

class Speedometer(Sensor):

    def measure(self):
        super().measure()
        # random speed stored as float
        self.last_measurement = random.random() * 30



class TemperatureSensor(Sensor):

    
    def measure(self):
        super().measure()
        # random speed stored as float
        self.last_measurement = random.random() * 10


class HeartFrequencySensor(Sensor):
    
     def measure(self):
        super().measure()
        # random heart frequency stored as float
        self.last_measurement = random.random() * 100


class BikeComputer(Sensor):

    def __init__(self):
        self.sensors = []

    def add_sensor(self, s: Sensor):
        self.sensors.append(s)



# main 
c = BikeComputer()
c.add_sensor(GpsSensor())
c.add_sensor(Speedometer())
c.add_sensor(HeartFrequencySensor())
c.add_sensor(TemperatureSensor())

# let all sensors measure
for s in c.sensors:
    s.measure()

# print current measurements
for s in c.sensors:
    print(s)



