import socket

def matrice(tab):
    for row in tab:
        print('|'.join(row))
    print()

def client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 3333)) # Connecte le client au serveur

    joueur1 = client_socket.recv(1024).decode().strip() # Reçoit le message du serveur
    joueur2 = 'X' if joueur1 == 'O' else 'O' # Définit le joueur 2
    joueur = joueur1
    print(f"Vous êtes le joueur {joueur1}")

    while True:
        reponse = client_socket.recv(1024).decode().strip()
        if reponse == "gagner":
            matrice(tab)
            print("Vous avez gagné !")
            break

    client_socket.close() 


server_ip = input("Entrer l'IP du serveur : ") # On demande à l'utilisateur de rentrer l'adresse IP du serveur
client(server_ip)


