from datetime import datetime, timedelta
from typing import List, Optional, Tuple
import random

class SensorVisitor:

    def handleSpeedometer(self, speed: float):
        pass

    def handleTemperature(self, temperature: float):
        pass

    def handleHeartFrequency(self, heart_freq: float):
        pass

    def handleGPS(self, gps: Tuple[float, float]):
        pass


class Sensor:

    def __init__(self):
        pass

    def accept(self, visitor: SensorVisitor):
        pass


class Display:


    def __init__(self):
        self.speed = 0.0
        self.average_speed = 0.0
        self.total_distance = 0.0
        self.current_distance = 0.0



class RoutePoint:

    def __init__(self, timestamp: datetime):
        self.timestamp = timestamp
        self.latitude = None
        self.longitude = None
        self.height = None
        self.heart_frequency = None
        self.temperature = None
        self.velocity = None
        self.next = None

    def __repr__(self):
        return f"{self.timestamp} ({self.latitude}, {self.longitude}) {self.height}m"


class AbstractRoute:

    def __init__(self):
        self.totalLength = None
        self.totalHeight = None
        self.averageSpeed = None
        self.maxSpeed = None
        self.usedCalories = None

    def calculateStatistic(self):
        pass


class RouteGroup(AbstractRoute):

    def __init__(self, name: str):
        self.name = name


class RouteIterator:

    def __init__(self, current: Optional[RoutePoint]):
        self.current = current

    def __next__(self):
        result = self.current
        if not result:
            raise StopIteration()
        self.current = result.next
        return result


class Route(AbstractRoute):

    def __init__(self):
        self.first = None
        self.last = None

    def add_point(self, point: RoutePoint):
        if not self.first:
            self.first = point
            self.last = point
        else:
            self.last.next = point
            self.last = point

    def __iter__(self):
        return RouteIterator(self.first)


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

# route = Route()
# skip_count = 0
# for line in file.readlines():
#     if skip_count > 1:
#         splt = line.split(",")
#         route.add_point(RoutePoint(timestamp=datetime.fromisoformat(splt[0]),
#                                    latitude=float(splt[1]),
#                                    longitude=float(splt[2]),
#                                    height=float(splt[3])))
#     skip_count += 1
#
# file.close()
#
# print(route.first)
# print(route.last)
#
# for point in route:
#     print(point)



sensor1 = GPSSensor()
sensor2 = TemperatureSensor()
sensor3 = Speedometer()
d = Display()
bc = BikeComputer(d, [sensor1, sensor2, sensor3])

bc.record()

for p in bc.current_route:
    print(p)
