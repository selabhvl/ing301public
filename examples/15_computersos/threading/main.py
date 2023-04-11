

import logging
import threading # https://superfastpython.com/threading-in-python/

from measurement import Measurement
from displaydevice import DisplayDevice
from sensordevice import SensorDevice

log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

measurement = Measurement()

display = DisplayDevice(1, measurement)
sensor = SensorDevice(measurement)

# a) limitation without threading
sensor.run()
display.run()

# b) with threading
# logging.info("Starting multi-threaded system")

# display.start()
# sensor.start()

# f) multiple displays - notify all

# second_display = DisplayDevice(2, measurement)
# second_display.start()

# c) wait for thread to finish
# display.join()
# sensor.join()
# second_display.join()

## d) locks

## e) condition variables

# logging.info("Stopping multi-threaded system")



