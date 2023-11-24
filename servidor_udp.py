import socket

def udp_server():
    # Criação do socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Endereço e porta do servidor
    server_address = ('localhost', 3030)
    
    # Associa o socket ao endereço e à porta
    server_socket.bind(server_address)
    
    print("Aguardando mensagem...")
    
    # Recebe e imprime a mensagem do cliente
    data, client_address = server_socket.recvfrom(1024)
    print("Mensagem do cliente:", data.decode('utf-8'))
    
    server_socket.close()


udp_server()
