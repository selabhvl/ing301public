import matplotlib.pyplot as plt

import gpscomputer


def plot_elevation(gps_data: list[tuple[int, float, float, float]]) -> None:

    elevations = list()

    for gps_point in gps_data:
        elevations.append(gps_point[3])

    x_points = list(range(1, len(elevations) + 1))

    plt.ylabel("Height m [" + str(len(elevations)) + "]")

    plt.plot(x_points, elevations)

    plt.show()


def plot_speeds(gps_data: list[tuple[int, float, float, float]]) -> None:

    speeds = gpscomputer.segment_speeds(gps_data)

    plt.ylabel("Speeds km/t [" + str(len(speeds)) + "]")

    x_points = list(range(1, len(speeds) + 1))

    plt.plot(x_points, speeds)

    plt.show()


def plot_route(gps_data: list[tuple[int, float, float, float]]) -> None:

    latitudes = list()
    longitudes = list()

    for gps_point in gps_data:
        latitudes.append(gps_point[1])
        longitudes.append(gps_point[2])

    plt.xlabel("Longitude [" + str(len(longitudes)) + "]")

    plt.ylabel("Latitude [" + str(len(latitudes))+ "]")

    plt.scatter(longitudes, latitudes)

    plt.show()

