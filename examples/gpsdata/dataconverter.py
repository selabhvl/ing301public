# Time format
# 2017-08-13T08:52:26.000Z

# convert time data string to seconds since midnight
def convert_time(date_time_str: str) -> int:

    START_POS = 11

    time_str = date_time_str[START_POS:]

    hr = int(time_str[0:2])
    mm = int(time_str[3:5])
    ss = int(time_str[6:8])

    secs = hr * 60 * 60 + mm * 60 + ss

    return secs


def convert_data(gps_csv_data: list[str]) -> list[tuple[int, float, float, float]] :

    gps_data = list()

    for line in gps_csv_data:

        secs = convert_time(line[0])
        latitude = float(line[1])
        longitude = float(line[2])
        elevation = float(line[3])

        gps_data.append((secs, latitude, longitude, elevation))

    return gps_data
