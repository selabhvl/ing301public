import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening")
    conn, addr = s.accept()
    with conn:
        print(f"The {addr} client connected")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print(str(data))
            conn.sendall(b"RECEIVED")

