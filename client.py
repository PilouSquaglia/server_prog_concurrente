import socket
import threading
import os

host, port = ('localhost', 12345)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receiveMessage():
    while True:
        message = mySocket.recv(1024).decode('utf-8')
        print("Autre client : " + message)

try:
    mySocket.connect((host, port))
    print("Je suis connecté ...")
except:
    print("Il y a eu un problème de connexion")
    sys.exit()

# Lancer un thread pour recevoir les messages de l'autre client
receive_thread = threading.Thread(target=receiveMessage)
receive_thread.start()

while True:
    message = input("Envoyez un message :\n")
    mySocket.send(message.encode('utf-8'))

mySocket.close()
