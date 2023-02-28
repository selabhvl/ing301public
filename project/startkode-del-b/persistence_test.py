import unittest
from pathlib import Path
from persistence import SmartHousePersistence, SmartHouseAnalytics
from main import load_demo_house
from datetime import datetime, date


class PersistenceTest(unittest.TestCase):
    file_path = str(Path(__file__).parent.absolute()) + "/db.sqlite"
    p = SmartHousePersistence(file_path)
    house = load_demo_house(p)

    def test_db_ok(self):
        self.assertTrue(PersistenceTest.p.check_tables())
        cursor = PersistenceTest.p.cursor
        cursor.execute("SELECT COUNT(*) FROM rooms;")
        result = int(cursor.fetchone()[0])
        self.assertEqual(12, result)
        cursor.execute("SELECT COUNT(*) FROM devices;")
        result = int(cursor.fetchone()[0])
        self.assertEqual(31, result)

    def test_loading_demo_house(self):
        rooms = PersistenceTest.house.get_all_rooms()
        self.assertEqual(12, len(rooms))
        devices = PersistenceTest.house.get_all_devices()
        self.assertEqual(31, len(devices))
        dev15 = PersistenceTest.house.find_device_by_serial_no("c28b6e75-d565-4678")
        kitchen = PersistenceTest.house.get_room_with_device(dev15)
        devices = PersistenceTest.house.get_all_devices_in_room(kitchen)
        self.assertEqual(8, len(devices))

    def test_updating_sensor_state(self):
        bedroom = PersistenceTest.house.get_room_with_device(PersistenceTest.house.find_device_by_serial_no("627ff5f3-f4f5-47bd"))
        PersistenceTest.house.turn_off_lights_in_room(bedroom)
        PersistenceTest.house.set_temperature_in_room(bedroom, 18.1)
        PersistenceTest.p.save()
        PersistenceTest.p.reconnect()
        house_loaded = load_demo_house(PersistenceTest.p)
        bedroom = house_loaded.get_room_with_device(house_loaded.find_device_by_serial_no("627ff5f3-f4f5-47bd"))
        self.assertEqual(
            "Aktuator(627ff5f3-f4f5-47bd) TYPE: Smart Lys STATUS: OFF PRODUCT DETAILS: Fritsch Group Alphazap 2",
            house_loaded.find_device_by_serial_no("627ff5f3-f4f5-47bd").__str__())
        self.assertEqual(
            "Aktuator(eed2cba8-eb13-4023) TYPE: Varmepumpe STATUS: 18.1 °C PRODUCT DETAILS: Osinski Inc Fintone XCX2FF",
            house_loaded.find_device_by_serial_no("eed2cba8-eb13-4023").__str__())
        house_loaded.turn_on_lights_in_room(bedroom)
        house_loaded.set_temperature_in_room(bedroom, 22.3)
        PersistenceTest.p.save()
        PersistenceTest.p.reconnect()
        house_loaded = load_demo_house(PersistenceTest.p)
        self.assertEqual(
            "Aktuator(627ff5f3-f4f5-47bd) TYPE: Smart Lys STATUS: ON PRODUCT DETAILS: Fritsch Group Alphazap 2",
            house_loaded.find_device_by_serial_no("627ff5f3-f4f5-47bd").__str__())
        self.assertEqual(
            "Aktuator(eed2cba8-eb13-4023) TYPE: Varmepumpe STATUS: 22.3 °C PRODUCT DETAILS: Osinski Inc Fintone XCX2FF",
            house_loaded.find_device_by_serial_no("eed2cba8-eb13-4023").__str__())

    def test_analytics_easy(self):
        actuator1 = PersistenceTest.house.find_device_by_serial_no("f11bb4fc-ba74-49cd")
        sensor3 = PersistenceTest.house.find_device_by_serial_no("4cb686fe-6448-4cf6")
        sensor8 = PersistenceTest.house.find_device_by_serial_no("e237beec-2675-4cb0")
        sensor12 = PersistenceTest.house.find_device_by_serial_no("d16d84de-79f1-4f9a")
        sensor21 = PersistenceTest.house.find_device_by_serial_no("8ceb53b2-e88f-4e8c")
        sensor28 = PersistenceTest.house.find_device_by_serial_no("481e94bd-ff50-40ea")
        anal = SmartHouseAnalytics(PersistenceTest.p)
        self.assertEqual(None, anal.get_most_recent_sensor_reading(actuator1))
        self.assertEqual(50.2717, anal.get_most_recent_sensor_reading(sensor3))
        self.assertEqual(8.3771, anal.get_most_recent_sensor_reading(sensor8))
        self.assertEqual(20.4913, anal.get_most_recent_sensor_reading(sensor12))
        self.assertEqual(55.2125, anal.get_most_recent_sensor_reading(sensor21))
        self.assertEqual(17.5987, anal.get_most_recent_sensor_reading(sensor28))

    def test_analytics_medium(self):
        anal = SmartHouseAnalytics(PersistenceTest.p)
        self.assertEqual("Entrance", anal.get_coldest_room())

        sensor12 = PersistenceTest.house.find_device_by_serial_no("d16d84de-79f1-4f9a")
        actuale = anal.get_sensor_readings_in_timespan(sensor12, datetime.fromisoformat("2023-02-14T13:35:00"),
                                                       datetime.fromisoformat("2023-02-14T13:42:00"))
        expected = [21.4786, 22.2991, 21.2237, 21.1827, 22.8388, 21.9996, 21.9651]
        self.assertEqual(expected, actuale)

        expected = {
            "Living Room / Kitchen": (15.0708, 24.1327, 20.606689623287576),
            "Entrance": (0.1589, 17.1905, 6.9318578742514925),
            "Master Bedroom": (12.0813, 21.3091, 16.473596511627903)
        }
        self.assertEqual(expected, anal.describe_temperature_in_rooms())

    def test_analytics_advanced(self):
        anal = SmartHouseAnalytics(PersistenceTest.p)
        expected = [8, 13, 17, 18, 19, 20, 21]
        self.assertEqual(expected,
                         anal.get_hours_when_humidity_above_average("Bathroom 1", date(year=2023, month=2, day=13)))
        expected = list(range(7, 24))
        self.assertEqual(expected,
                         anal.get_hours_when_humidity_above_average("Bathroom 2", date(year=2023, month=2, day=14)))


if __name__ == '__main__':
    unittest.main()
