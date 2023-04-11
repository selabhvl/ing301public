import time
import logging

from threading import Thread
from measurement import Measurement


# class DisplayDevice(Thread):
class DisplayDevice(Thread):

    def __init__(self, did: int, measurement: Measurement):
        super().__init__()
        self.did = did
        self.measurement = measurement

    def display(self):

        logging.info(f"DISPLAY DEVICE [{self.did}]: {self.measurement}")

    def run(self):

        COUNT = 10

        logging.info(f'Display [{self.did}] started')

        for i in range(0, COUNT):

            self.display()

            time.sleep(1) # not needed when condition variables are introduced

        logging.info(f'Display [{self.did}]  stopped')
