

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

# a) without threading
# display.display()

# sensor.read()
# time.sleep(3)
# display.display()

# sensor.read()
# time.sleep(3)
# display.display()

# b) limitation without threading
#display.run()
#sensor.run()

# c) with threading
logging.info("Starting multi-threaded system")

seconddisplay = DisplayDevice(2, measurement)

display.start()

seconddisplay.start()

sensor.start()

# d) wait for thread to finish
display.join()
seconddisplay.join()
sensor.join()

logging.info("Stopping multi-threaded system")

# e) locks

# f) signalling with condition variables eliminating sleep in measurement?

update_available = threading.Condition()

# g) multiple displays - notify all





