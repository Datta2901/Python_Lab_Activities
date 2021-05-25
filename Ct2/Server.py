
import socket

def server_program():
    host = socket.gethostname()
    port = 5000  
    server_socket = socket.socket() 
    server_socket.bind((host, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True: 
        conn.send("Meassge from server".encode())
        break;  
    conn.close() 

server_program()
