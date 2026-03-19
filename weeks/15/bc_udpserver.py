import socket
import sys
from gpspoint import GPSPoint

def main(server_host, server_port):

    SERVER_BUFFER_SIZE = 2048

    route = []
    udp_server_socket = None
    try:
        # Creating an UDP socket based on the IP protocol
        udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        udp_server_socket.bind((server_host, server_port))
        print(f"UDP server: {server_host}:{server_port}")


        while True:
            print("UDP server waiting")
            bytes_received, sender_addr = udp_server_socket.recvfrom(SERVER_BUFFER_SIZE)

            message = bytes_received.decode('UTF-8')

            # print(f"UDP server received: '{message}' from {sender_addr}")

            gps_point = GPSPoint.from_json(message)
            print(f"UDP client GPS point received: {gps_point} from {sender_addr}")

            route.append(gps_point)
            print(f"Current route now contains {len(route)} points")

    except KeyboardInterrupt:
        for gps_point in route:
            print(gps_point)
    finally:
        if udp_server_socket:
            udp_server_socket.close()



if __name__ == "__main__":
    if len(sys.argv) == 3:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
    else:
        print("<serverhost> and <serverport> unspecified! Falling back to '127.0.0.1' and '8000' defaults")
        print("Usage: python udpserver_cmd <serverhost> <serverport>")
        server_host = "127.0.0.1"
        server_port = 8000

    main(server_host, server_port)
