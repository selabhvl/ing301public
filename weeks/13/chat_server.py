import socket

server_address = "127.0.0.1"
server_port = 9002
server_socket = socket.socket()

server_socket.bind((server_address, server_port))
server_socket.listen(1)

print(f"Server listening on {server_address}:{server_port}")

conn_socket, client_address = server_socket.accept()

print(f"Server accepted connection from {client_address}")

msg : str = ""
while msg !=  "bye":
    print("Server waiting to receive: ")
    data = conn_socket.recv(1024)
    msg = data.decode("utf-8")
    print(f"Server received: " + msg)
    conn_socket.sendall("OK".encode("utf-8"))

conn_socket.close()
server_socket.close()

print("Server shut down")