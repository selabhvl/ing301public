import socket

server_address = "127.0.0.1"
server_port = 9002
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((server_address, server_port))
server.listen(1)

print(f"Server listening on {server_address}:{server_port}")

conn, client_address = server.accept()

print(f"Server accepted connection from {client_address}")

msg : str = ""
while msg !=  "bye":
    print("Server waiting to receive: ")
    data = conn.recv(1024)
    msg = data.decode("utf-8")
    print(f"Server received: " + msg)
    conn.sendall("OK".encode("utf-8"))

conn.close()
server.close()

print("Server shutting down")