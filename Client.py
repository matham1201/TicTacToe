import socket

def client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 3333)) # Connecte le client au serveur

    client_socket.close() 


server_ip = input("Enter server IP: ") # On demande à l'utilisateur de rentrer l'adresse IP du serveur
client(server_ip)
