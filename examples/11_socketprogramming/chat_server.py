import socket

server_address = "127.0.0.1"
server_port = 9002
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((server_address, server_port))
server.listen(1)

print(f"Server listening on {server_address}:{server_port}")

conn, client_address = server.accept()

print(f"Established connection to {client_address}")

msg : str = ""
while msg !=  "bye":
    msg = input("server: ")
    conn.sendall(msg.encode("utf-8"))
    data = conn.recv(1024)
    print(f"client: " + data.decode("utf-8"))

conn.sendall("bye".encode("utf-8"))
conn.close()
server.close()

print("server shutting down")