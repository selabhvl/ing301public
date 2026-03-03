import random
from datetime import datetime, timedelta
import json
import pickle
import sqlite3

class Point:

    def __init__(self, timestamp: datetime, latitude: float, longitude: float):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"{self.timestamp.isoformat()} ({round(self.latitude, 4)}, {round(self.longitude, 4)})"

    def to_json(self):
        result = {}
        result["timestamp"] = self.timestamp.isoformat()
        result["latitude"] = self.latitude
        result["longitude"] = self.longitude
        return result

class Route:

    def __init__(self):
        self.points = []

    def add(self, point: Point):
        self.points.append(point)

    def __repr__(self):
        return f"Route ({len(self.points)} segments):\n" + '\n'.join([f"#{i+1}: {p}" for i, p in zip(range(len(self.points)), self.points) ])

    def save(self):
        # Skrive til CSV
        fil = open("route.csv", "wt")
        fil.write("timestamp,latitude,longitude\n")
        for p in self.points:
            fil.write(f"{p.timestamp},{p.latitude},{p.longitude}\n")
        fil.close()
        print("Written to route.csv!")
        # skrive til JSON
        fil = open('route.json', "w+")
        json_points = []
        for p in self.points:
            json_points.append(p.to_json())
        json_objekt = {
            "points": json_points
        }
        json.dump(json_objekt, fil, indent=3)
        fil.close()
        print("Written to route.json")
        # Write pickle
        fil = open('route.picke', "wb")
        pickle.dump(self, fil)
        fil.close()
        print("Written to route.pickle")
        # Write to sqlite
        connection = sqlite3.Connection("route.sqlite")
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE routes(timestamp text, latitude number, longitude number )")

        for p in self.points:
            cursor.execute(f"INSERT INTO routes VALUES ('{p.timestamp}', {p.latitude}, {p.longitude})")

        cursor.close()
        connection.commit()
        connection.close()
        print("written to route.sqlite")
        return




class GpsSensor:

    def __init__(self,
                 initial_timestamp: datetime = datetime(2025, 2, 18, 14, 0),
                 recording_delta: timedelta = timedelta(seconds=30),
                 start_latitude: float = 60.369270,
                 start_longitude: float = 5.349365):
        self.timestamp = initial_timestamp
        self.recording_delta = recording_delta
        self.latitude = start_latitude
        self.longitude = start_longitude

    def sample(self) -> Point:
        result = Point(self.timestamp, self.latitude, self.longitude)
        xmomentum = random.random() * 0.1 - 0.05
        ymomentum = random.random() * 0.1 - 0.05
        self.timestamp += self.recording_delta
        self.latitude += xmomentum
        self.longitude += ymomentum
        return result


def main():
    is_active = True
    sensor = GpsSensor()
    route = Route()
    # TODO: her kunne jeg lastet inn CSV
    fil = open("route.picke", "rb")
    route = pickle.load(fil)
    fil.close()
    while is_active:
        print("---- Bike Computer ----\nSelect option:\n1. Track route\n2. Show Route\n3. Save\n4.Quit\n")
        user_input = input(">>> ")
        if not user_input.isdigit() and int(user_input) in {1, 2, 3, 4}:
            print(f"Unrecognized input: '{user_input}'")
        else:
            selected_option = int(user_input)
            if selected_option == 1:
                no_sample = int(input("How many segments do you want to track: "))
                for _ in range(no_sample):
                    route.add(sensor.sample())
                print(f"recorded {no_sample} segments")
            elif selected_option ==2:
                print(route)
            elif selected_option == 3:
                route.save()
            else:
                is_active = False
    print("shutting down")

if __name__ == "__main__":
    main()
