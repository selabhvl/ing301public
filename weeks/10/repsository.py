from sqlite3 import Connection

class Sensor:

    def __init__(self, sensor_id, name):
        self.id = sensor_id
        self.name = name

class SensorRepository:

    def __init__(self, connection: Connection):
        self.connection = connection


    # CRUD = CREATE READ UPDATE DELETE

    def create_sensor(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT max(id) from sensors")
        last_id = cursor.fetchone()[0]
        next_id = last_id + 1
        cursor.execute(f"INSERT INTO sensors (id, sensor_type) VALUES (?, ?)", (next_id, name))
        self.connection.commit()


    def read_all_sensors(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, sensor_type FROM sensors")
        result = []
        for row in cursor.fetchall():
            result.append(Sensor(row[0], row[1]))
        return result

    def read_by_id(self):
        pass

    def read_by_name(self):
        pass

    def update_sensor(self):
        pass

    def delete_sensor(self):
        pass

def main():
    connection = Connection("/Users/past-madm/Projects/teaching/ing301/ing301public/weeks/09/db.sqlite")
    repo = SensorRepository(connection)
    for s in repo.read_all_sensors():
        print(s.name)
    repo.create_sensor("temperature")

main()