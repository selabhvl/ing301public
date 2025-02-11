# Python Modul importering
import haversine

print(haversine.R)

# filstien vil være annerledes på din maskin
# også husk på Windows må du erstatte hver enkelt "\" med en dobbelt "\\"
file = open("./weeks/04/gpslogs/short.csv")
innhold = file.read()
linjer = innhold.split("\n")
sist_lengd = float(linjer[1].split(",")[1])
sist_bredd = float(linjer[1].split(",")[2])
max_hoyde = float(linjer[1].split(",")[3])
total_distanse = 0
for linje in linjer[2:]:
    linje_delt = linje.split(",")
    current_lengd = float(linje_delt[1])
    current_bredd = float(linje_delt[2])
    current_hoyde = float(linje_delt[3])
    distanse = haversine.distance(sist_bredd, sist_lengd, current_bredd, current_lengd)
    sist_lengd = current_lengd
    sist_bredd = current_bredd
    total_distanse += distanse
    if current_hoyde > max_hoyde:
        max_hoyde = current_hoyde
    #print(linje_delt[3])
print("Høyste punkt på turen var på " + str(max_hoyde) + "m")
print("Turen var på " + str(round(total_distanse / 1000, 2)) + "km")

file.close()