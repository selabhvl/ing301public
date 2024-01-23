import haversine

class GPSPoint:
    
    today = "tirsdag"

    # detter er uvanlig
    def say_hi():
        print("Hei")

    # konstruktor
    # vanlig
    def __init__(self, time: str, lat: float, long: float, height: float):
        self.time = time
        self.lat = lat 
        self.long = long 
        self.height = height

    
    def distance_to(self, other):
        return haversine.distance(self.lat, self.long, other.lat, other.long)
        


# vil ha...
point = GPSPoint(time="2017-08-13T08:52:26.000",
                 lat=60.385390,
                 long=5.217217,
                 height=61.9)
point_b = GPSPoint(time="2017-08-13T08:53:00.000",
                 lat=60.385588,
                 long=5.217857,
                 height=56.2)


result = point.distance_to(point_b)
print("Distanse mellom a og b:" + str(result))

