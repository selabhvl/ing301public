import time
from threading import Thread

from measurement import Measurement


class DisplayDevice(Thread):

    def __init__(self, measurement: Measurement):
        self.measurement = measurement
        super().__init__()

    def display(self):

        print(f"DISPLAY: {self.measurement}")

    def run(self):

        COUNT = 10

        print("Display started")

        for i in range(0, COUNT):

            self.display()

            time.sleep(1)

        print("Display stopped")
