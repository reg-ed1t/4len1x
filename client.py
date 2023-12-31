import socket
from colorama import just_fix_windows_console
import termcolor

just_fix_windows_console()

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))
        self.nickName = input("Enter nickname ") + ":"
        self.nickname = colored(self.nickName, nicknameColor.lower(), attrs=["bold"])
        self.nicknameColor = input("Enter nickname color:  ")

    def run(self):
        try:
            while True:
                message = self.nickname + input("Enter message ")
                self.client.sendall(message.encode())
                data = self.client.recv(1024)
                print(data.decode())
        except Exception as e:
            print(e)


def main():
    ip = input("ip: ")
    port = int(input("port: "))
    client = Client(ip, port)
    client.run()


if __name__ == "__main__":
    main()
