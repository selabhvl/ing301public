from datetime import datetime


class GpsCoord:
    def __init__(self, time, lat, lon, elevation,
                  accuracy, bearing,speed,satellites,
                  provider, hdop, vdop, pdop, geoidheight,
                  ageofdgpsdata, dgpsid, activity, battery, annotation):
        self.battery = self.tryparser(battery, float)
        self.activity = activity
        self.dgpsid = dgpsid
        self.ageofdgpsdata = ageofdgpsdata
        self.geoidheight = geoidheight
        self.pdop = self.tryparser(pdop, float)
        self.vdop = self.tryparser(vdop, float)
        self.hdop = self.tryparser(hdop, float)
        self.provider = provider
        self.satellites = self.tryparser(satellites, int)
        self.annotation = annotation
        self.speed = self.tryparser(speed, float)
        self.time = self.tryparser(time, datetime.fromisoformat)
        self.lat = self.tryparser(lat, float)
        self.lon = self.tryparser(lon, float)
        self.elevation = self.tryparser(elevation, float)
        self.accuracy = self.tryparser(accuracy, float)
        self.bearing = self.tryparser(bearing, float)

    @staticmethod
    def tryparser(x, _class):
        try:
            y = _class(x)
        except:
            y = None
        return y


def convert_data(gps_csv_data):
    # 0time, 1lat, 2lon, 3elevation, 4accuracy, 5bearing, 6speed, 7satellites, 8provider, 9hdop, 10vdop, 11pdop, 12geoidheight, 13ageofdgpsdata, 14dgpsid, 15activity, 16battery, 17annotation
    gpscoordslist = []
    for item in gps_csv_data:
        tempvar = GpsCoord(item[0], item[1], item[2], item[3], item[4],
                           item[5], item[6], item[7], item[8], item[9],
                           item[10], item[11], item[12], item[13],
                           item[14], item[15], item[16], item[17])
        # all gps records not containing time will be discarded
        if tempvar.time is not None:
            gpscoordslist.append(tempvar)
    # sorts list based on the class attribute time
    gpscoordslist.sort(key=lambda time: time.time, reverse=False)
    return gpscoordslist