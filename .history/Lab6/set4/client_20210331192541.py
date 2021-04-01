/
import time
import socket
# import sys

print("Welcome to chat room\n")
time.sleep(1)

s=socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

print(host,"(",ip,")\n")
host = "192.168.0.8"
name = input(str("\nEnter your name: "))
port = input(str("\nEnter your port: "))
print("\nTrying to connect to ",host,"(",ip,")\n")
time.sleep(1)
s.connect((host,int(port)))
print("Connected...\n")

s.send(name.encode())
sName = s.recv(1024)
sName = sName.decode()
print(sName," has joined the chatroom\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(sName,": ",message)
    message = input(str("Me: "))
    if message == '1':
        message = "Left chatroom"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
     