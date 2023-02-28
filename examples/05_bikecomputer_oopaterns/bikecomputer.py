from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from sensors import Sensor, SensorVisitor, GPSSensor, TemperatureSensor, Speedometer
from routes import RoutePoint, Route


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

    def __init__(self, current_route: Route):
        self.current_route = current_route

    def calculate_speed(self) -> float:
        # Beregne tidsforskjell mellom to siste punkt og distance
        # self.current_route.
        pass


class RecordSensorValues(SensorVisitor):

    def __init__(self, to_record_on: RoutePoint):
        self.to_record_on = to_record_on

    def handleSpeedometer(self, speed: float):
        self.to_record_on.velocity = speed

    def handleTemperature(self, temperature: float):
        self.to_record_on.temperature = temperature

    def handleHeartFrequency(self, heart_freq: float):
        self.to_record_on.heart_frequency = heart_freq

    def handleGPS(self, gps: Tuple[float, float]):
        self.to_record_on.latitude = gps[0]
        self.to_record_on.longitude = gps[1]


class BikeComputer:

    def __init__(self, display: Display, sensors: List[Sensor]):
        self.display = display
        self.sensors = sensors
        self.speed_strategy = None
        self.current_route = Route()

    def record(self):
        for clock in range(0, 1000, 10):
            p = RoutePoint(timestamp=datetime.utcnow() + timedelta(seconds=clock))
            visitor = RecordSensorValues(p)
            for sensor in self.sensors:
                sensor.accept(visitor)
            self.current_route.add_point(p)

    def update_speed(self):
        # TODO dangerous right now
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

print("From file")
for point in route:
    print(point)

sensor1 = GPSSensor()
sensor2 = TemperatureSensor()
sensor3 = Speedometer()
d = Display()
bc = BikeComputer(d, [sensor1, sensor2, sensor3])

bc.record()
print("From recording")
for p in bc.current_route:
    print(p)
