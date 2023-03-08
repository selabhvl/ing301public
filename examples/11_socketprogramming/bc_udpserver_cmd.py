import sys
from bc_udpserver import main

if __name__ == "__main__":
    if len(sys.argv) == 3:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        main(server_host, server_port)
    else:
        print("Usage: python3 udpserver_cmd <serverhost> <serverport>")

