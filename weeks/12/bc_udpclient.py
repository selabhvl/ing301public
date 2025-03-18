import sys
import socket
import time

from gpssensor import GPSSensor

# https://docs.python.org/3/library/socket.html

def main(server_host: str, server_port: int, no_points: int):
    sensor = GPSSensor(1)
    print(f"UDP client started, trying to reach: {server_host}:{server_port}")

    # create UDP socket for sending data
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    for _ in range(0, no_points):
        gps_point = sensor.read()
        print(f"UDP client GPS point to be sent: {gps_point}")
        message = gps_point.to_json()


        # Encode message string into bytes using UDT-8 (the default)
        bytes_to_send = str.encode(message)

        # send the data
        udp_client_socket.sendto(bytes_to_send, (server_host, server_port))

        # wait 2 seconds before sending next
        time.sleep(2)

    # close the UDP socket
    udp_client_socket.close()
    print("UDP client stopped")



if __name__ == "__main__":
    if len(sys.argv) == 4:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        no_points = int(sys.argv[3])
    else:
        print("<serverhost>, <serverport> and <number of points> unspecified! Falling back to '127.0.0.1', '8000' and '10' defaults")
        print("Usage: python3 udpclient_cmd <serverhost> <serverport> <number of points>")
        server_host = "127.0.0.1"
        server_port = 8000
        no_points = 10
    main(server_host, server_port, no_points)
