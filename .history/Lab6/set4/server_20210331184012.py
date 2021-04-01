import time,socket,sys
import _thread

print('\nWelcome to Chat Room\n')

def startchat(num,port):
    s=socket.socket()
    host=socket.gethostname()
    ip=socket.gethostbyname(host)
    
    s.bind((host,int(port)))
    print(host,"(",ip,")\n")
    name=input(str("Enter your name: "))
    
    s.listen(1)
    print("\nWaiting for incoming connections...\n")
    conn,addr=s.accept()
    print("Received connection from ", addr[0],"(",addr[1],")\n")
    
    sName = conn.recv(1024)
    sName = sName.decode()
    print(sName,"has connected to the chatroom\n
    print(Enter 1 to exit the chatroom\n")
    conn.send(name.encode())
    
    while True:
        print("You are talking to ",num)
        print("Me",num,": ",end="")
        message = input()
        if message == '1':
            message = "Left the chat room!"
            conn.send(message.encode())
            print("\n")
            break
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(sName,num,": ",message)
        
        
try:
    noOfChats = int(input("Enter the number of chats that you want to receive: "))
    for i in range(noOfChats):
        _thread.start_new_thread(startchat,(i+1,1234+i))
except:
    print("Error during threading")
    
while True:
    pass