from sqlite3 import Connection
import pickle

fil = open("data/route1.pickle", "rb")
route = pickle.load(fil)
fil.close()

connection = Connection("data/database.sqlite")

cursor = connection.cursor()

for point in route:
    cursor.execute(f"INSERT INTO route (ts, latitude, longitude, height, route_id) VALUES ('{point.timestamp}', {point.latitude}, {point.longitude}, {point.height}, 1);")

connection.commit()
cursor.close()
