import sys

from bc_udpclient import main

if __name__ == "__main__":
    if len(sys.argv) == 4:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        no_points = int(sys.argv[3])
        main(server_host, server_port, no_points)
    else:
        print("Usage: python3 udpclient_cmd <serverhost> <serverport> <number of points>")
