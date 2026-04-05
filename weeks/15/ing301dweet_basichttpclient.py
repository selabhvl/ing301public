import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("dweetr.io", 80))

#sock.sendall(b"GET get/latest/dweet/for/ing301 HTTP/1.1\r\nHost:dweetr.io\r\n\r\n")

sock.sendall(b"GET get/latest/dweet/for/ing301")

response = sock.recv(4096)
sock.close()
print(response.decode())
