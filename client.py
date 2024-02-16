import socket
import threading

def receive_messages(client_socket):
    while True:
        # Receive data from the server
        data = client_socket.recv(1024).decode()
        print('Received from server:', data)

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12347  # The same port as used by the server

    # Connect to the server
    client_socket.connect((host, port))

    # Create a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Send data to the server
        message = input("Enter message to send to server: ")
        client_socket.send(message.encode())

        # If the user wants to exit, send 'bye' and break the loop
        if message.lower() == 'bye':
            break

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    main()
