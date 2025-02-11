# Python Modul importering
import haversine
from datetime import datetime, timedelta

class Point:
    
    def __init__(self, linje: str):
        delt_opp = linje.split(",")
        self.ts = datetime.fromisoformat(delt_opp[0])
        self.latitude = float(delt_opp[1])
        self.longitude = float(delt_opp[2])
        self.height = float(delt_opp[3])

    def distance_to(self, other):
        return haversine.distance(self.longitude, self.latitude, other.longitude, other.latitude)

    def time_diff(self, other):
        return other.ts - self.ts

    def __sub__(self, other):
        return self.distance_to(other)
    
    def __lt__(self, other):
        return  self.height < other.height


def read_file(fil):
    file = open(fil)
    result = []
    innhold = file.read()
    linjer = innhold.split("\n")
    for linje in linjer[1:]:
        result.append(Point(linje))
    file.close()
    return result



# filstien vil være annerledes på din maskin
# også husk på Windows må du erstatte hver enkelt "\" med en dobbelt "\\"

filnavn = "./weeks/04/gpslogs/short.csv"
points = read_file(filnavn)

last = points[0]
total_distanse = 0
max_hoyde = last
totalt_time = timedelta(seconds=0)
for current in points[1:]:

    distance = current - last
    totalt_time += last.time_diff(current)

    # regne ut distanse
    sist = current
    total_distanse += distance

    # regne maks høyde
    if max_hoyde < current:
        max_hoyde = current

print("Høyste punkt på turen var på " + str(max_hoyde.height) + "m")
print("Turen var på " + str(round(total_distanse / 1000, 2)) + "km")
print("Turen tok " + str(totalt_time) + "")

