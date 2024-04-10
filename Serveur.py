import socket

def main():
    socketServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServ.bind(('10.44.16.174', 3333)) # Définit l'adresse IP et le port du serveur
    socketServ.listen(10) # Le serveur accepte jusqu'à 10 connexions (en attente)
    print("Serveur en attente de connexion...")
    
    connection, client = socketServ.accept() # Accepte la connexion du client

    print("Connecté avec : ", client)

    connection.close()
    socketServ.close()

main()
