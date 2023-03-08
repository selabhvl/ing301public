import json


class GPSPoint:

    def __init__(self, pid, long, lat, height):
        self.pid = pid
        self.lat = lat
        self.long = long
        self.height = height

    def __str__(self):
        return "(" + str(self.pid) + "," + str(self.lat) + "," + str(self.long) + "," + str(self.height) + ")"

    # https://levelup.gitconnected.com/how-to-deserialize-json-to-custom-class-objects-in-python-d8b92949cd3b
    def to_json(self):
        gps_point_encoded = json.dumps(self.__dict__)
        return gps_point_encoded

    @staticmethod
    def json_decoder(json_gps_point_dict):
        return GPSPoint(json_gps_point_dict['pid'],
                        json_gps_point_dict['lat'],
                        json_gps_point_dict['long'],
                        json_gps_point_dict['height'])

    @staticmethod
    def from_json(json_gps_point_str: str):

        json_gps_point_dict = json.loads(json_gps_point_str)
        gps_point = GPSPoint.json_decoder(json_gps_point_dict)

        return gps_point


