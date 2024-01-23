import haversine

fil = open("/Users/past-madm/Projects/teaching/ing301/ing301public/examples/02_gpsdata/gpslogs/short.csv", "r", encoding="UTF-8")
liste = fil.readlines()

def calculate_total_climb(liste):
    current = float(liste[1].split(',')[3])
    result = 0
    for l in liste[2:]:
        linje_elemeter = l.split(',')
        height = float(linje_elemeter[3])
        if height > current:
            diff = height - current
            result += diff
        current = height
    return result


def calculate_distance(liste):
    current_lat = float(liste[1].split(',')[1])
    current_lon = float(liste[1].split(',')[2])
    result = 0
    for l in liste[2:]:
        linje_elemeter = l.split(',')
        lat = float(linje_elemeter[1])
        lon = float(linje_elemeter[2])
        diff = haversine.distance(current_lat, current_lon, lat, lon)
        result += diff
        current_lat = lat
        current_lon = lon
    return result
    


print("Total climb " + str(calculate_total_climb(liste)))
print("Total distance " + str(calculate_distance(liste)))