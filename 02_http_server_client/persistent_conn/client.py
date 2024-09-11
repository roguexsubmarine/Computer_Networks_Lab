import socket

# host and port to connect to server
HOST = '127.0.0.1'  
PORT = 8080 

# socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:

    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.sendall(request.encode('utf-8'))

    # Receive the response from the server
    response = client_socket.recv(4096).decode('utf-8')
    print(f"Response from server:\n{response}")

client_socket.close()

