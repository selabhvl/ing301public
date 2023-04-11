import time
import logging

from threading import Thread

from measurement import Measurement
from sensor import Sensor

# class SensorDevice(Thread):


class SensorDevice:

    def __init__(self, measurement: Measurement):
        super().__init__()
        self.sensor = Sensor()
        self.measurement = measurement

    def read(self):

        new_temp = self.sensor.read()
        self.measurement.update(new_temp)

        logging.info(f'SENSOR DEVICE: {new_temp}')

        return new_temp

    def run(self):

        COUNT = 10

        logging.info("Sensor started")

        for i in range(0, COUNT):

            read_temp = self.read()

            time.sleep(3)

        logging.info("Sensor stopped")


