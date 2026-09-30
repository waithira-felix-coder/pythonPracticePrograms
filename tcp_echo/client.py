import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

print(f"Connected to TCP Echo Server at {HOST}:{PORT}")
print("Type a message and press Enter.")
print("Type 'exit' to close the connection.")

while True:
    message = input("You: ")

    # Stop the client
    if message.lower() == "exit":
        break

    # Send the message to the server
    client_socket.sendall(message.encode("utf-8"))

    # Receive the echoed response
    data = client_socket.recv(1024)

    print(f"Server Echo: {data.decode('utf-8')}")

# Close the connection
client_socket.close()

print("Client disconnected.")