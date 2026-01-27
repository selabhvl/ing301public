import haversine
class GPSPoint:

    def __init__(self, linje):
        linje_delt = linje.split(",")
        self.time = linje_delt[0]
        self.lat = float(linje_delt[1])
        self.long = float(linje_delt[2])
        self.height = float(linje_delt[3])
            
    def say_hi(self):
        return "Hi from " + str(id(self))
    
    def distance(self, other):
        return haversine.distance(self.lat, self.long, other.lat, other.lat)

p1 = GPSPoint("2017-08-14T05:23:35.000,60.385920,5.218073,48.6")
p2 = GPSPoint("2017-08-14T05:23:46.000,60.385540,5.217313,48.9")
#print(type(p1)) # klasse
#print(id(p1)) # memory address
#print(dir(p1)) # egenskaper
#print(GPSPoint.say_hi(p1)) # lang variante 
#print(p2.say_hi()) # kort variate

#p1.lat = 60.5
#print(p1.lat)
#print(dir(p1))
#print(p2.lat)

avstand = p1.distance(p2)
print(avstand)