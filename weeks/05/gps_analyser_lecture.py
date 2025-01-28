# Python Modul importering
import haversine

class Point:
    
    def __init__(self, linje: str):
        delt_opp = linje.split(",")
        self.ts = delt_opp[0] 
        self.latitude = float(delt_opp[1])
        self.longitude = float(delt_opp[2])
        self.height = float(delt_opp[3])


# p = Point("asdfhsdi", 60.1, 5.9, 100.0) # constructor av Point
# q = Point("34rhweafj", 60.5, 5.8, 8.0)

# print(p.latitude)
# print(p.longitude)


# filstien vil være annerledes på din maskin
# også husk på Windows må du erstatte hver enkelt "\" med en dobbelt "\\"
file = open("/Users/past-madm/Projects/teaching/ing301/ing301public/weeks/04/gpslogs/short.csv")
innhold = file.read()
linjer = innhold.split("\n")
last = Point(linjer[1])
total_distanse = 0
max_hoyde = 0
for linje in linjer[2:]:
    current = Point(linje)
    # regne ut distanse
    distanse = haversine.distance(last.longitude, last.latitude, current.longitude, current.latitude)
    sist = current

    total_distanse += distanse
    # regne maks høyde
    if current.height > max_hoyde:
        max_hoyde = current.height
    #print(linje_delt[3])
print("Høyste punkt på turen var på " + str(max_hoyde) + "m")
print("Turen var på " + str(round(total_distanse / 1000, 2)) + "km")

file.close()