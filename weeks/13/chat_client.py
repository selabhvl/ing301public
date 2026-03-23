import socket

client_socket = socket.socket()

server_address = "127.0.0.1"
server_port = 9002

client_socket.connect((server_address, server_port))
print(f"Client connected to {server_address}")

msg = ""
while msg != "bye":
    msg = input("Client: ")
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024)
    print(f"From server: {data.decode()}")

print("Connection terminated.")

client_socket.close()
