import socket

client033 = socket.socket()
host033 = socket.gethostname()
port033 = 9997
client033.connect((host033, port033))

print('Send a message to server:')
sendtoserver = input()
client033.send(sendtoserver.encode())
print('\n')
print(client033.recv(1024).decode())