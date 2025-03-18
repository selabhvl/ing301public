import socket
import sys
import json

from gpssensor import GPSSensor


def main(server_host, server_port, no_points):

    sensor = GPSSensor(1)
    route = []

    print(f"TCP client {server_host}:{server_port}")

    print("TCP client generating GPS points ...")

    for _ in range(0, no_points):

        gps_point = sensor.read()

        route.append(gps_point)

    print("TCP client sending GPS points ...")
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # encode the route into a json string
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
    if len(sys.argv) == 4:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        no_points = int(sys.argv[3])
        main(server_host, server_port, no_points)
    elif len(sys.argv) == 1:
        NO_POINTS = 10
        main("127.0.0.1", 8000, NO_POINTS)
    else:
        print("Usage: python3 bc_tcpclient [<serverhost> <serverport>]")


