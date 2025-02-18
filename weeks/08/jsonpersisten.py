from bikecomputer import Point, GpsSensor
import json

sensor = GpsSensor()
point = sensor.sample()

#print(json.dumps({ "a_list": [42, 23, 17, 3.1415], "a_name": "Ole"}))

print(json.dumps(point.to_json()))
