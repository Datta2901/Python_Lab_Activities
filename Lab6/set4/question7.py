import threading
import time
in_buffer = 0
out_of_buffer = 0
in_buffer_Lock = threading.Lock()
out_of_buffer_Lock = threading.Lock()
buffer = threading.Semaphore(7)
def Produce_item():
        buffer.acquire()
        global in_buffer_Lock
        in_buffer_Lock.acquire()
        global in_buffer
        in_buffer = in_buffer+1
        in_buffer_Lock.release()
        print("In buffer : %d"%(in_buffer))
def Consume_Item():
        buffer.release()
        global out_of_buffer_Lock
        out_of_buffer_Lock.acquire()
        global out_of_buffer
        out_of_buffer = out_of_buffer + 1
        out_of_buffer_Lock.release()
        print("Out of buffer: %d"%(out_of_buffer))

def enter_items():
    for i in range(15):
        time.sleep(1)
        producing_item = threading.Thread(target=Produce_item)
        producing_item.start()

def consume_items():
    for j in range(10):
        time.sleep(1)
        consuming_item = threading.Thread(target=Consume_Item)
        consuming_item.start()
enter_items()
consume_items()