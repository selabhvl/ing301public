import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("dweet.io", 80))
sock.sendall(b"GET get/latest/dweet/for/ing301 HTTP/1.1\r\nHost:dweet.io\r\n\r\n")

response = sock.recv(4096)
sock.close()
print(response.decode())
