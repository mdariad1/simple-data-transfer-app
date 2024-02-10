import socket
import os

def send_file(conn, filename):
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            conn.sendall(data)

def receive_file(conn, filename):
    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening...")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        command, filename = data.split()
        if command == 'upload':
            receive_file(conn, f'database/{filename}')
        elif command == 'download':
            send_file(conn, f'database/{filename}')
        conn.close()

if __name__ == "__main__":
    start_server()
