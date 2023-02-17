import socket
import threading

host, port = ('localhost', 12345)
Format = "utf-8"

class Client:
    def __init__(self, name):
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.receive_thread = threading.Thread(target=self.receiveMessage)
        self.receive_thread.start()

    def sendMessage(self, message):
        if not isinstance(self.socket, socket.socket):
            print("Erreur: le socket n'est pas valide")
            return

        if self.socket.fileno() == -1:
            print("Erreur: le socket est fermé")
            return
        print("##########################{}#########################".format(message))
        self.socket.send(message.encode(Format))

    def receiveMessage(self):
        while True:
            try:
                message = self.socket.recv(1024).decode(Format)
                if message:
                    print(message)
                # else:
                #     self.socket.close()
                #     break
            except:
                self.socket.close()
                break

name = input("Entrez votre nom : ")
client = Client(name)

while True:
    message = input()
    client.sendMessage(f"{name}: {message}")
