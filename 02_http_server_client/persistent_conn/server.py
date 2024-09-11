import socket

# host and port for the server
HOST = '127.0.0.1'
PORT = 8080     

# socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Start listening
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    request = client_socket.recv(1024).decode('utf-8')
    print(f"Request received:\n{request}")

    response = "Server is running !"

    # Send the response to the client
    client_socket.sendall(response.encode('utf-8'))

    while response:
        response = input("\nEnter prompt : ")
        client_socket.sendall(response.encode('utf-8'))

    
    client_socket.close()

