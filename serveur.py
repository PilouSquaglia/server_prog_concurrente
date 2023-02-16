import socket
import threading

host, port =('', 12345)
#Création d’une socket (IPv4, TCP)
mySocket = socket.socket(socket.AF_INET,
    socket.SOCK_STREAM)
#Identification IPv4 (IP, Port)
mySocket.bind((host, port))
#nombre de rejet acceptés
mySocket.listen(3)
numClient = 1
Format = "Utf8"
threads = []

class Client(threading.Thread):
    def __init__(self, conn, address):
        threading.Thread.__init__(self)
        self.conn = conn
        self.address = address

    def run(self):
        file_name = self.conn.recv(2048).decode(Format)
        try:
            fp = open(file_name, 'rb')
            self.conn.send(fp.read())
            print("Fichier envoyé !")
        except FileNotFoundError:
            print(f"Le fichier {file_name} n'existe pas.")

print("Attente de nouveau client")
while True:
    # Attente du client et récupération de ses données
    conn, address = mySocket.accept()
    print("Le client numéro {} s'est connecté : {}".format(numClient, address))
    numClient += 1

    # Créer un nouveau thread pour gérer le client
    threadClient = Client(conn, address)
    threadClient.start()
    threads.append(threadClient)

    # Attendre que tous les threads soient terminés
    for t in threads:
        t.join()

    # Fermer le client
    conn.close()

    # Vérifier si le serveur doit continuer à écouter
    continuer = input("Voulez-vous continuer ? (o/n) ")
    if continuer.lower() == 'n':
        break

# Fermer le serveur
mySocket.close()
