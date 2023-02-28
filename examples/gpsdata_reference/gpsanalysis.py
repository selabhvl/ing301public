from datetime import datetime
import haversine

file = open('gpslogs/short.csv', 'r')
i = 0

gps_points = []

for line in file.readlines():
    if i > 1:
        split_line = line.split(',')
        gps_points.append(split_line[:4])
    i += 1


highest_point = 0
for point in gps_points:
    elevation = float(point[3])
    if elevation > highest_point:
        highest_point = elevation

print(f"Highest Peak: {highest_point} masl")

start = datetime.fromisoformat(gps_points[0][0])
end = datetime.fromisoformat(gps_points[-1][0])

total_time = end - start
print(f"Total Time: {total_time}")

total_distance = 0
for i in range(0, len(gps_points) - 1):
    from_point = gps_points[i]
    to_point = gps_points[i + 1]
    lat_from = float(from_point[1])
    long_from = float(from_point[2])
    lat_to = float(to_point[1])
    long_to = float(to_point[2])
    distance = haversine.distance(lat_from, long_from, lat_to, long_to)
    total_distance += distance

total_distance_km = total_distance / 1000.0
print("Total distance: {:.2f} km".format(total_distance_km))

print("Average speed: {:.2f} km/h".format(total_distance_km / (total_time.total_seconds() / (60 * 60))))
