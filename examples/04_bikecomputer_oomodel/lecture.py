from typing import List



class Sensor:

    def __init__(self, id: str) -> None:
        self.id = id
    

class GPSSensor(Sensor):

    def __init__(self, id, time_now) -> None:
        super().__init__(id)
        self.time_now = time_now

    def record_position(self):
        pass 


class Speedometer(Sensor):
    pass 

class TemperatureSensor(Sensor):
    pass

class HeartFrequencySensor(Sensor):
    pass 

class GPSPoint:

    def __init__(self, timestamp: str, latitude: float, longitude: float, height: float):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.height = height



class BikeComputer:

    def __init__(self, sensors: List[Sensor]):
        self.sensors = sensors
