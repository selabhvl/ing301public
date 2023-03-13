import socket
import time

import common
from gpssensor import GPSSensor

# https://docs.python.org/3/library/socket.html
# https://realpython.com/python-sockets/


def main(server_host: str, server_port: int, no_points: int):

    sensor = GPSSensor(1)

    print(f"UDP client started: {server_host}:{server_port}")

    # create UDP socket for sending data
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    for i in range(0, no_points):

        gps_point = sensor.read()

        print("UDP client GPS point to be sent:" + str(gps_point))

        message = gps_point.to_json()

        # print("UDP client sending: " + str(message))

        # Encode message string into bytes using UDT-8 (the default)
        bytes_to_send = str.encode(message)

        # send the data
        udp_client_socket.sendto(bytes_to_send, (server_host, server_port))

        time.sleep(2)

    # close the UDP socket
    udp_client_socket.close()

    print("UDP client stopped")


if __name__ == "__main__":

    NO_POINTS = 10

    main(common.SERVER_HOST, common.SERVER_PORT, NO_POINTS)
