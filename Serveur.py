import socket
import random

def afficher(tab):
    print("-------------")
    print("|", tab[0], "|", tab[1], "|", tab[2], "|")
    print("-------------")
    print("|", tab[3], "|", tab[4], "|", tab[5], "|")
    print("-------------")
    print("|", tab[6], "|", tab[7], "|", tab[8], "|")
    print("-------------")

def main():
    socketServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServ.bind(('10.44.16.174', 3333)) # Définit l'adresse IP et le port du serveur
    socketServ.listen(10) # Le serveur accepte jusqu'à 10 connexions (en attente)
    print("Serveur en attente de connexion...")
    
    connection, client = socketServ.accept() # Accepte la connexion du client

    print("Connecté avec : ", client)

    # Jeu
    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    joueur1 = random.choice(['X', 'O'])
    connection.sendall(f"{joueur1}\n".encode())
    joueur2 = 'X' if joueur1 == 'O' else 'O'
    joueur = joueur1

    while True:
        print(f"Joueur {joueur}")
        choix = connection.recv(1024).decode().strip()
        choix = int(choix)
        
        if tab[choix - 1] in ["X", "O"]:
            print("Case déjà prise")
            connection.sendall("invalide".encode())
        elif choix < 1 or choix > 9:
            print("Case invalide")
            connection.sendall("invalide".encode())            
        else:
            tab[choix - 1] = joueur
            joueur = joueur1 if joueur == joueur2 else joueur2
            connection.sendall("valide".encode())
            
            
        afficher(tab)
        
        lignes_gagnantes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]      
        ]
        
        for ligne in lignes_gagnantes:
            if tab[ligne[0]] == tab[ligne[1]] == tab[ligne[2]]:
                print(f"Joueur {joueur} a gagné")
                connection.sendall("Gagné".encode())
                break
        else:
            if all(symbole in ["X", "O"] for symbole in tab):
                print("Match nul")
                connection.sendall("égalité".encode())
                break

    connection.close()
    socketServ.close()

main()
