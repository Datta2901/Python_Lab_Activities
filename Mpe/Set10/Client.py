# question 3
import socket


def client_program():
    host = socket.gethostname()  
    port = 5000  

    client_socket = socket.socket()  
    client_socket.connect((host, port))

    message =input("Enter a number")
    
    client_socket.send(message.encode())  
    data = client_socket.recv(1024).decode()  
    print('Received from server: ' + data)  
    print(data)

    client_socket.close()  


if __name__ == '__main__':
    client_program()
