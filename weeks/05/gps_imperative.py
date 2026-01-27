# Vi trenger noen hjelpefunksjoner fra Python sitt "standard bibliotek"
import math

# constant: earth radius in meters
R = 6371000

# Hjelpfunksjon for å beregne avstand mellom to koordinater i meter
def distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> float:
    """
    Distance between two GPS points in meters as per the haversine formula.

    Reading link:
    https://en.wikipedia.org/wiki/Haversine_formula
    """
    phi_1 = math.radians(latitude1)
    phi_2 = math.radians(latitude2)

    delta_phi = math.radians(latitude2 - latitude1)
    delta_delta = math.radians(longitude2 - longitude1)

    a = math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + math.cos(phi_1) * math.cos(phi_2) * (
            math.sin(delta_delta / 2) * math.sin(delta_delta / 2))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = R * c

    return d

# test
# Vi åpner en fil
file = open("weeks/05/gpslog.csv")
# Hele innhold blir lest inn i en variabel
innhold = file.read()
# Vi lukker filen igjen
file.close()
# Vi deler opp innholdet ved linjeskift. `linjer` er en liste av streng.
linjer = innhold.split("\n")

# Den første linjen (dvs. indeks 0) i en CSV fil inneholder kolonnenavn
kolonner = linjer[0]
if not kolonner.startswith("time,lat,lon,elevation"):
    # enkel feilbehandling
    raise ValueError("inputtfil har feil format!")

# Den andre linjen er den første linjen med data
linje = linjer[1]
# Hver linje består av "celler" som er delt med komma
linje_delt = linje.split(",")

# Kolonnene med indeks 1,2,3 inneholder lengdegrad, breddegrad, og høyde over havet (alle må koverteres fra streng til tall) 
lengdegrad = float(linje_delt[1]) # lat
breddegrad = float(linje_delt[2]) # lon
max_hoyde = float(linje_delt[3]) # elevation

# Aggregasjonsvariabel
total_distanse = 0

# Løkke som går gjennom resterende linjer
for linje in linjer[2:]:

    
    # håndtere tomme linjer
    if len(linje) == 0:
        continue

    # steg 1: uthenting
    linje_delt = linje.split(",")


    neste_lengdegrad = float(linje_delt[1])
    neste_breddegrad = float(linje_delt[2])
    neste_hoyde = float(linje_delt[3])

    # steg 2: aggregasjon max(elevation)
    if neste_hoyde > max_hoyde:
        max_hoyde = neste_hoyde

    # steg 3: aggregasjon av distanser mellom koordinater
    # begynn med å beregne avstand
    distanse = distance(breddegrad, lengdegrad, neste_breddegrad, neste_lengdegrad)
    # summere opp
    total_distanse += distanse

    # oppdatere nåværende koordinate
    lengdegrad = neste_lengdegrad
    breddegrad = neste_breddegrad

# Avslutte med å skrive informasjon til skjerm
print("Høyste punkt på turen var på " + str(max_hoyde) + "m")
print("Turen var på " + str(round(total_distanse / 1000, 2)) + "km")


