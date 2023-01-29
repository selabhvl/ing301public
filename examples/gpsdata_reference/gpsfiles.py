"""
GPSDATA CSV FORMAT
time,lat,lon,elevation,accuracy,bearing,speed,satellites,
provider,hdop,vdop,pdop,geoidheight,ageofdgpsdata,dgpsid,activity,battery,annotation
"""
from pathlib import Path
import csv


def read_gps_file(filename):

    file = open(str(Path(__file__).parent.absolute()) + "/gpslogs/" + filename + ".csv", 'r')

    gps_data = csv.reader(file)
    gps_points = list(gps_data)

    file.close()

    return gps_points[2:]




