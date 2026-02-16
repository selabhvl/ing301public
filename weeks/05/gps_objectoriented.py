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

file = open("weeks/05/gpslog.csv")
innhold = file.read()
file.close()

linjer = innhold.split("\n")

# Den første linjen (dvs. indeks 0) i en CSV fil inneholder kolonnenavn
kolonner = linjer[0]
if not kolonner.startswith("time,lat,lon,elevation"):
    # enkel feilbehandling
    raise ValueError("inputtfil har feil format!")

siste_punkt = GPSPoint(linjer[1])

# Aggregasjonsvariabler
max_hoyde = siste_punkt.height # elevation
total_distanse = 0

# Løkke som går gjennom resterende linjer
for linje in linjer[2:]:

    
    # håndtere tomme linjer
    if len(linje) == 0:
        continue

    # steg 1: uthenting
    neste_punkt = GPSPoint(linje)


    # steg 2: aggregasjon max(elevation)
    if neste_punkt.height > max_hoyde:
        max_hoyde = neste_punkt.height

    # summere opp
    total_distanse += siste_punkt.distance(neste_punkt)

    # oppdatere siste punkt
    siste_punkt = neste_punkt

# Avslutte med å skrive informasjon til skjerm
print("Høyste punkt på turen var på " + str(max_hoyde) + "m")
print("Turen var på " + str(round(total_distanse / 1000, 2)) + "km")

