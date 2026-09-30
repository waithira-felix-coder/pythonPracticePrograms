import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow quick reuse of the port after restarting the server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(1)

print(f"TCP Echo Server is running on {HOST}:{PORT}")
print("Waiting for a client connection...")

# Accept a client connection
client_socket, client_address = server_socket.accept()

print(f"Client connected from {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024)

    # If no data is received, the client has disconnected
    if not data:
        break

    message = data.decode("utf-8")

    print(f"Client: {message}")

    # Send the same message back to the client
    client_socket.sendall(data)

# Close the connections
client_socket.close()
server_socket.close()

print("Server stopped.")