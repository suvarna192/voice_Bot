import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print('Received from client:', data)

        # If the client sends 'bye', close the connection
        if data.lower() == 'bye':
            break

        # Echo back the received data
        client_socket.send(data.encode())

    # Close the connection with the client
    client_socket.close()

def send_message(client_socket, message):
    client_socket.send(message.encode())

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12347 # Reserve a port for your service.

    # Bind to the port
    server_socket.bind((host, port))

    # Now wait for client connection.
    server_socket.listen(5)

    print("Server listening on {}:{}".format(host, port))

    while True:
        # Establish connection with client.
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

        # Send a welcome message to the client
        send_message(client_socket, "Welcome to the server!")

        # Start a new thread to handle server-to-client messages
        server_send_thread = threading.Thread(target=handle_server_send, args=(client_socket,))
        server_send_thread.start()

def handle_server_send(client_socket):
    while True:
        message = input("Enter message to send to client: ")
        send_message(client_socket, message)

if __name__ == '__main__':
    main()
