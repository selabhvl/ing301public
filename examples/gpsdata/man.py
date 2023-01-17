from datetime

file = open("gpslogs/short.csv", 'r')
lines = file.readlines()
counter = 0
gps_point = []
for line in lines:
    if counter > 0:
        gps_point.append(line)
    counter += 1

print(gps_point)

first = gps_point[0]
first_split = first.split(',')
first_timestamp = first_split[0]

last = gps_point[-1]
last_split = last.split(',')
last_timestamp = datetime.fromisoformat(last_split[0])


print(first.split(','))
print(type(first))


