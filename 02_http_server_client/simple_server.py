import socket

# Define the host and port for the server
HOST = '127.0.0.1'  # Localhost
PORT = 9000        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")



while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")


    # Receive the request from the client
    response = """\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple HTTP Server</title>
</head>
<body>
    <h1>Server is running !</h1>
    <p>Connection established.</p>
</body>
</html>
"""
    request = client_socket.recv(1024).decode('utf-8')
    
    print(f"Request received:\n{request}")

    # Prepare a simple HTTP response

    # Send the response to the client
    client_socket.sendall(response.encode('utf-8'))

    # Close the client connection
    client_socket.close()



