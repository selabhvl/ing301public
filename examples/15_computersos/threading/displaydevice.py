import time
import logging

from threading import Thread
from measurement import Measurement


class DisplayDevice(Thread):

    def __init__(self, measurement: Measurement):
        super().__init__()
        self.measurement = measurement

    def display(self):

        logging.info(f"DISPLAY: {self.measurement}")

    def run(self):

        COUNT = 10

        logging.info("Display started")

        for i in range(0, COUNT):

            self.display()

            time.sleep(1)

        logging.info("Display stopped")
