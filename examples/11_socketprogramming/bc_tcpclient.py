import socket
import sys
import json

import common
from gpssensor import GPSSensor


# https://pythonexamples.org/python-json/
def main(server_host, server_port, no_points):

    sensor = GPSSensor(1)
    route = list()

    print(f"TCP client {server_host}:{server_port}")

    print("TCP client generating GPS points ...")

    for i in range(0, no_points):

        gps_point = sensor.read()

        route.append(gps_point)

    print("TCP client sending GPS points ...")
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # encode the route into a json string
    # uses Python list comprehension: https://www.w3schools.com/python/python_lists_comprehension.asp
    route_json_str = json.dumps([gps_point.__dict__ for gps_point in route])

    print(route_json_str)

    # encode the json string into bytes
    route_bytes_to_send = route_json_str.encode()

    route_bytes_len = len(route_bytes_to_send)
    print(f"Route data length : {route_bytes_len}")

    tcp_client_socket.connect((server_host, server_port))

    # send first data_len as 4 bytes in big-endian representation (network byte order)
    tcp_client_socket.sendall(route_bytes_len.to_bytes(4, 'big'))

    # then send the bytes representing the route
    tcp_client_socket.sendall(route_bytes_to_send)

    tcp_client_socket.close()


if __name__ == "__main__":

    NO_POINTS = 10

    if len(sys.argv) == 3:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        main(server_host, server_port, NO_POINTS)
    elif len(sys.argv) == 1:
        main(common.SERVER_HOST, common.SERVER_PORT, NO_POINTS)
    else:
        print("Usage: python3 tcpserver [<serverhost> <serverport>]")


