import threading,time,_thread

def print_021(delay,counter):
    if counter==51:
        return
    
    T1=threading.Thread(target=print_021,args=(1,counter+1))
    T1.start()
    T1.join() 
    print(f"Hello from Thread: {counter}")
    time.sleep(delay)


T1=threading.Thread(target=print_021,args=(1,1))
T1.start()
T1.join() 

print("Exiting Threads")