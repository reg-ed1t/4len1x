import threading
import datetime
import socket


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.ip}:{self.port}")

    def handle_client(self, conn, addr):
        try:
            print(f"[NEW CONNECTION] {addr} connected.")

            connected = True
            while connected:
                msg = conn.recv(1024)
                print(f"[{addr}] {msg.decode()}")
                conn.send("Message received".encode())

            conn.close()
        except Exception as e:
            with open("log.txt", "a") as file:
                timestamp = datetime.datetime.now().isoformat(
                    sep=" ", timespec="seconds"
                )
                file.write(f"[{timestamp}] Error: {str(e)}\n")
        finally:
            conn.close()

    def start(self):
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def main():
    server = Server("localhost", 1234)
    server.start()


if __name__ == "__main__":
    main()
