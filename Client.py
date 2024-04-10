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
        choix = input(f"Joueur {joueur}, entrez (ligne,colonne) : ")
        client_socket.sendall(choix.encode())

        reponse = client_socket.recv(1024).decode().strip()
        if reponse == "gagner":
            matrice(tab)
            print("Vous avez gagné !")
            break
        elif reponse == "égalité":
            matrice(tab)
            print("Égalité !")
            break
        elif reponse == "perdu":
            matrice(tab)
            print("Vous avez perdu !")
            break
        elif reponse == "valide":
            row, col = map(int, choix.split(','))
            if joueur == joueur1:
                tab[row][col] = joueur1
                joueur = joueur2
            else:
                tab[row][col] = joueur2
                joueur = joueur1
            matrice(tab)
        elif reponse == "invalide":
            print("Coup invalide, réessayez !")


    client_socket.close() 

if __name__ == "__main__":
    server_ip = input("Entrer l'IP du serveur : ") # On demande à l'utilisateur de rentrer l'adresse IP du serveur
    client(server_ip)


