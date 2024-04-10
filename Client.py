import socket

def afficher(tab):
    print("-------------")
    print("|", tab[0], "|", tab[1], "|", tab[2], "|")
    print("-------------")
    print("|", tab[3], "|", tab[4], "|", tab[5], "|")
    print("-------------")
    print("|", tab[6], "|", tab[7], "|", tab[8], "|")
    print("-------------")

def client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 3333)) # Connecte le client au serveur

    joueur1 = client_socket.recv(1024).decode().strip() # Reçoit le message du serveur
    joueur2 = 'X' if joueur1 == 'O' else 'O' # Définit le joueur 2
    joueur = joueur1

    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Vous êtes le joueur {joueur1}")
    afficher(tab)

    while True:
        choix = input(f"Joueur {joueur}, le numéro de la case : ")
        client_socket.sendall(choix.encode())
        choix = int(choix)

        reponse = client_socket.recv(1024).decode().strip()

        if reponse == "Gagné": # Bug ici 
            afficher(tab)
            joueur = joueur1 if joueur == joueur2 else joueur2 # Bug ici
            print(f"{joueur} : Vous avez gagné !")
            break
        elif reponse == "égalité":
            afficher(tab)
            print("Égalité !")
            break
        elif reponse == "valide":
            tab[choix - 1] = joueur
            joueur = joueur1 if joueur == joueur2 else joueur2
            afficher(tab)
        elif reponse == "invalide":
            print("Coup invalide, réessayez !")



    client_socket.close() 

server_ip = input("Entrer l'IP du serveur : ") # On demande à l'utilisateur de rentrer l'adresse IP du serveur
client(server_ip)


