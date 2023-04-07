import time
from threading import Thread

from measurement import Measurement
from sensor import Sensor


class SensorDevice(Thread):

    def __init__(self, measurement: Measurement):
        self.sensor = Sensor()
        self.measurement = measurement
        super().__init__()

    def read(self):

        new_temp = self.sensor.read()
        self.measurement.update(new_temp)

        return self.measurement.current_temp

    def run(self):

        COUNT = 10

        print("Sensor started")

        for i in range(0, COUNT):

            read_temp = self.sensor.read()
            print(f'SENSOR: {read_temp}')

            time.sleep(2)

        print("Sensor stopped")


