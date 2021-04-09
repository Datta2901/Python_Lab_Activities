# question 3
import socket


def client_program():
    host = socket.gethostname()  
    port = 5000  

    client_socket = socket.socket()  
    client_socket.connect((host, port))
    while True:
        data = client_socket.recv(1024).decode()  
        print('Received from server: ' + data) 
        break; 
    client_socket.close()  

if __name__ == '__main__':
    client_program()
