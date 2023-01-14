from datetime import datetime

file = open("gpslogs/short.csv", 'r')
lines = file.readlines()
counter = 0
gps_points = []
for line in lines:
    if counter > 0:
        gps_points.append(line)
    counter += 1


first = gps_points[0]
first_split = first.split(',')
first_timestamp = datetime.fromisoformat(first_split[0])

last = gps_points[-1]
last_split = last.split(',')
last_timestamp = datetime.fromisoformat(last_split[0])
print(first_timestamp)
print(last_timestamp)
print(last_timestamp - first_timestamp)

max_height = 0
for point in gps_points:
    current_height = float(point.split(',')[3])
    if max_height < current_height:
        max_height = current_height

print(max_height)
