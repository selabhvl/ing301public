from measurement import Measurement
from sensor import Sensor

class SensorDevice:

    def __init__(self, measurement: Measurement):
        self.sensor = Sensor()
        self.measurement = measurement

    def read(self):

        new_temp = self.sensor.read()
        self.measurement.update(new_temp)

        return new_temp

    def run(self):

        COUNT = 10

        print("Sensor started")

        for i in range(0, COUNT):
            read_temp = self.sensor.read()
            print(f'SENSOR: {read_temp}')

        print("Sensor stopped")


