import socket

def udp_client():
    # Criação do socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Endereço e porta do servidor
    server_address = ('localhost', 3030)
    
    try:
    
        message = "Olá, servidor!"
        client_socket.sendto(message.encode('utf-8'), server_address)
        
    finally:
      
        client_socket.close()

# Chama a função do cliente UDP
udp_client()
