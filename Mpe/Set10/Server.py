
import socket

def fact(data):
    prod = 1
    for i in range(1, data + 1):
        prod *= i
    return prod

    

def server_program():
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket() 
    server_socket.bind((host, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    data = conn.recv(1024).decode()
    print("from connected user: " + str(data))
    n = int(data)
    answer = fact(n)
    conn.send(str(answer).encode())
        
    conn.close()  


if __name__ == '__main__':
    server_program()
