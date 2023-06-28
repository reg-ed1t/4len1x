import threading
import datetime
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
def handle_client(conn, addr):
    try:
        print(f'[NEW CONNECTION] {addr} connected.')

        connected = True
        while connected:
            msg = conn.recv(1024)
            if msg == b'/exit':
                connected = False
            print(f'[{addr}] {msg.decode()}')
            conn.send('Message received'.encode())

        conn.close()
    except Exception as e:
        with open('log.txt', 'a') as file:
            timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
            file.write(f'[{timestamp}] Error: {str(e)}\n')

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

def logc():
    try:
        with open("log.txt", 'x'):
            print("Файл для логов успешно создан!")
    except FileExistsError:
        pass
print('[STARTING] Server is starting...')
logc()
start()
