import pickle
from bikecomputer import Point, GpsSensor
sensor = GpsSensor()
point = sensor.sample()


#fil = open("database.pickle", mode="wb")
#pickle.dump(point, fil)
#fil.close()

fil = open("database.pickle", mode="rb")
point = pickle.load(fil)
fil.close()

print(point)
