import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = "127.0.0.1"
server_port = 9002

client_socket.connect((server_address, server_port))

msg = ""
while msg != "bye":
    msg = input("client: ")
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024)
    print(f"server: {data.decode()}")

print("Connection terminated.")

client_socket.close()
