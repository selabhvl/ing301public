import socket

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

try:
    while True:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        print(request)

        # Send HTTP response
        response = 'HTTP/1.0 200 OK\n\nHello World'
        client_connection.sendall(response.encode())
        client_connection.close()

except KeyboardInterrupt:
    print(" Ctrl-C pressed")

finally:
    # Close socket
    print("Terminating")
    server_socket.close()
