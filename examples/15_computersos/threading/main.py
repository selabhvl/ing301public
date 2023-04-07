# https://superfastpython.com/threading-in-python/

# https://github.com/lmkr/dat110-labsolutions/tree/main/week3/src/no/hvl/dat110/week3/exercise4

# udvide med min / maks slik det går an å få race condition

from measurement import Measurement
from displaydevice import DisplayDevice
from SensorDevice import SensorDevice

measurement = Measurement()

display = DisplayDevice(measurement)
sensor = SensorDevice(measurement)

# a) without threading
display.display()
sensor.read()
display.display()

# b) limitation without threading
display.run()
sensor.run()



