import socket
import threading

host, port = ('', 12345)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((host, port))
mySocket.listen(2)

class Client(threading.Thread):
    def __init__(self, conn, address, client_num):
        threading.Thread.__init__(self)
        self.conn = conn
        self.address = address
        self.client_num = client_num

    def run(self):
        print("Client {} connecté : {}".format(self.client_num, self.address))
        message = self.conn.recv(2048).decode('utf-8')
        try:
            self.sendMessage(message)
        except NameError:
            print("Pas de message envoyé")

    def sendMessage(self, message):
        other_client = clients[0] if self == clients[1] else clients[1]
        other_client.conn.send(message.encode('utf-8'))

    def __del__(self):
        self.conn.close()

# Créer une liste pour stocker les clients connectés
clients = []

print("Attente de deux clients...")
for i in range(2):
    conn, address = mySocket.accept()
    client = Client(conn, address, i + 1)
    client.start()
    clients.append(client)

# Attendre que les threads soient terminés
for client in clients:
    client.join()

# Fermer les connexions
for client in clients:
    client.conn.close()
mySocket.close()

