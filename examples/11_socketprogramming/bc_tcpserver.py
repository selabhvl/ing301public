import socket
import sys
import json

import common
from gpspoint import GPSPoint


def main(server_host, server_port):

    # create and bind socket for incoming TCP connections
    welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    welcome_socket.bind((server_host, server_port))

    print(f"TCP server {server_host}:{server_port}")

    # enable server to accept connections on welcome socket
    welcome_socket.listen()

    route = list()

    try:

        while True:

            print("TCP server waiting for incoming connections ...")

            connection, addr = welcome_socket.accept()

            print(f"Client connected from {addr}")

            # receive first four bytes which specifies len of bytes for the route
            route_len_bytes = connection.recv(4)

            # decode the first four bytes into a integer
            route_bytes_len = int.from_bytes(route_len_bytes, 'big')

            print(f"Route data length : {route_bytes_len}")

            # receive the required number of bytes
            bytes_remaining = route_bytes_len
            route_bytes = bytearray()

            # need to read in a while-loop since TCP is stream-oriented and we may not
            # be able to receive all bytes in one recv method call
            while bytes_remaining > 0:

                bytes_next = connection.recv(bytes_remaining)

                route_bytes.extend(bytes_next)
                bytes_remaining = bytes_remaining - len(bytes_next)

            # decode the route bytes into a string
            route_json_str = bytes(route_bytes).decode('UTF-8')

            print(route_json_str)

            # decode the json representation into a route (list of GPSPoint objects)
            json_gps_point_dict_list = json.loads(route_json_str)

            route = list()

            for gps_point_dict in json_gps_point_dict_list:
                gps_point = GPSPoint.json_decoder(gps_point_dict)
                route.append(gps_point)

            connection.close()

    except KeyboardInterrupt:
        for gps_point in route:
            print(gps_point)
    finally:
        if welcome_socket:
            welcome_socket.close()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        main(server_host, server_port)
    elif len(sys.argv) == 1:
        server_host = common.SERVER_HOST
        server_port = common.SERVER_PORT
        main(server_host, server_port)
    else:
        print("Usage: python3 tcpserver [<serverhost> <serverport>]")



