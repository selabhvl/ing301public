import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

GPSPOINT = "2017-09-08T13:49:50.000Z,60.377625,5.328243,56.2,15.1,158.25,7.297732,0,gps,99.99,99.99,99.99,,,,,98.0,"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(GPSPOINT,'utf-8'))
    data = s.recv(1024)

print(f"Received {data!r}")
