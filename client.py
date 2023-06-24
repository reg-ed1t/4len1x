import socket

IP = 'localhost'
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

while True:
    msg = input('Enter message ')
    client.send(msg.encode())
    data = client.recv(1024)
    print(data.decode())

client.close()
