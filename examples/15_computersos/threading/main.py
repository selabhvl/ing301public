# https://superfastpython.com/threading-in-python/

# https://github.com/lmkr/dat110-labsolutions/tree/main/week3/src/no/hvl/dat110/week3/exercise4

# udvide med min / maks slik det går an å få race condition
# TODO: swith to using logging and not print?

import time
import logging

from measurement import Measurement
from displaydevice import DisplayDevice
from sensordevice import SensorDevice

log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

measurement = Measurement()

display = DisplayDevice(measurement)
sensor = SensorDevice(measurement)

# a) without threading
display.display()

sensor.read()
time.sleep(3)
display.display()

sensor.read()
time.sleep(3)
display.display()

# b) limitation without threading
#display.run()
#sensor.run()

# c) with threading
logging.info("Starting multi-threaded system")

display.start()
sensor.start()

# d) wait for thread to finish
display.join()
sensor.join()

logging.info("Stopping multi-threaded system")

display.display()





