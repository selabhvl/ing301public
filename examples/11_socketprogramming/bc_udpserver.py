import socket
from typing import Optional, List, Dict, Tuple

from gpspoint import GPSPoint
import common


def main(server_host, server_port):

    SERVER_BUFFER_SIZE = 2048

    try:
        udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        udp_server_socket.bind((server_host, server_port))

        print(f"UDP server: {server_host}:{server_port}")

        route: List[GPSPoint] = list()

        while True:

            print("UDP server waiting")

            bytes_received, sender_addr = udp_server_socket.recvfrom(SERVER_BUFFER_SIZE)

            message = bytes_received.decode('UTF-8')

            # print("UDP server received: " + message)

            gps_point = GPSPoint.from_json(message)

            print("UDP client GPS point received:" + str(gps_point))

            route.append(gps_point)

            print(f"Current route now contains {len(route)} points")

    except KeyboardInterrupt:
        for gps_point in route:
            print(gps_point)
    finally:
        if udp_server_socket:
            udp_server_socket.close()


if __name__ == "__main__":
    main(common.SERVER_HOST, common.SERVER_PORT)
