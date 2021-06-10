import socket

sob033 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host033 = socket.gethostname()
port033 = 9997
sob033.bind((host033, port033))
sob033.listen(6)
print("I am the server!")

while True:
    conn33, add33 = sob033.accept()
    sentbyclient = conn33.recv(1024).decode()
    if sentbyclient == 'ping' or sentbyclient == 'PING':
        sentbyserver = 'SERVER: Pong!'
        conn33.send(sentbyserver.encode())
    else:
        sentbyserv = 'SERVER: DROPPED!!!'
        conn33.send(sentbyserv.encode())
    conn33.close()