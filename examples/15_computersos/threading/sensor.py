import time
import math

TEMP_RANGE = 20


class Sensor:

    @staticmethod
    def read():

        temp = round(math.sin(time.time() / 10) * TEMP_RANGE, 1)
        return temp

