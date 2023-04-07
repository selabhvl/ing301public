import time
import math
import logging

TEMP_RANGE = 20


class Sensor:

    @staticmethod
    def read():

        temp = round(math.sin(time.time() / 10) * TEMP_RANGE, 1)
        # logging.info(f'SENSOR: {temp}')
        return temp

