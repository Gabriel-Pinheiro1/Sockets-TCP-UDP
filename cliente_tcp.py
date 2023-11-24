import socket

def tcp_client():
    # Criação do socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Endereço do servidor e porta
    server_address = ('localhost', 3300)
    
    try:
        # Tenta se conectar ao servidor
        client_socket.connect(server_address)
        
        # Envia uma mensagem ao servidor
        message = "Olá, servidor!"
        client_socket.sendall(message.encode('utf-8'))
        
    except socket.error as e:
        print(f"Erro de socket: {e}")

    finally:
        client_socket.close()

tcp_client()
