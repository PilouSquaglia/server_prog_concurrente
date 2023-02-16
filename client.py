import socket
import sys

Format = "Utf8"
host, port =('localhost', 12345)
#Création d’une socket (IPv4, TCP)
mySocket = socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM)
try :
    #Demande de connexion au serveur
    mySocket.connect((host, port))
    print("Je suis connecté ...")
except :
    print("Il y a eu un problème de connexion")
    sys.exit()

while True:
    file_name = input("Donnez le nom du fichier\n")
    mySocket.send(file_name.encode(Format))
    file_name = "data/{}".format(file_name)
    file = mySocket.recv(999999).decode(Format)
    with open(file_name, "wb") as name:
        name.write(file)
    print("Fichier écrit ! ")
    break

mySocket.close()