import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.example.com", 80))
sock.sendall(b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n")

response = sock.recv(4096)
sock.close()
print(response.decode())
