from datetime import datetime
import haversine

# Reading Points from file
file = open("/Users/emilpetersson/Skole/ING301/ing301public/examples/gpsdata/gpslogs/short.csv", 'r')
lines = file.readlines()
counter = 0
gps_points = []
for line in lines:
    if counter >= 1:
        split_line = line.split(',')
        gps_points.append(split_line[:4])
    counter += 1

# Calculating total ride time
first = gps_points[0]
first_timestamp = datetime.fromisoformat(first[0])

last = gps_points[-1]
last_timestamp = datetime.fromisoformat(last[0])
total_time = last_timestamp - first_timestamp
print(f"Total Time: {total_time}")

# Finding highest elevation of the ride
max_height = 0
for point in gps_points:
    current_height = float(point[3])
    if max_height < current_height:
        max_height = current_height

print(f"Highest Peak: {max_height} masl")


class GPSPoint:
    
    def __init__(self, time, longitude, latitude, elevation):
        self.lat = latitude
        self.long = longitude
        self.time = time
        self.elevation = elevation
        
    def si_hei():
        print("Hello")
    
    
        


# Finding total distance of the ride
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


if __name__ == "__main__":
    p = GPSPoint(time="2017-08-13T08:52:26.000", longitude=12.345, latitude=12.345, elevation=12.345)
    print(p)
    
