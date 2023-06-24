import socket
import threading

IP = 'localhost'
PORT = 1234

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg = conn.recv(1024)
        if msg == b'quit':
            connected = False
        print(f'[{addr}] {msg.decode()}')
        conn.send('Message received'.encode())

    conn.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    print(f'[LISTENING] Server is listening on {IP}:{PORT}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

print('[STARTING] Server is starting...')
start()
