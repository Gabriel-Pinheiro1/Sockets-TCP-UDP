import socket
def tcp_server():
    # Criação do socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Associa o socket ao endereço e à porta
    server_address = ('localhost', 3300)
    server_socket.bind(server_address)
    
    # Coloca o socket em modo de escuta
    server_socket.listen(1)
    print("Aguardando conexão...")
    
    # Aceita a conexão do cliente
    client_socket, client_address = server_socket.accept()
    print("Conexão aceita de:", client_address)
    
    # Recebe e imprime a mensagem do cliente
    data = client_socket.recv(1024)
    print("Mensagem do cliente:", data.decode('utf-8'))
    
    client_socket.close()

tcp_server()
