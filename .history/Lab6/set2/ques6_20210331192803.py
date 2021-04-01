import threading, time
def print_time_(threadName, delay, counter):# passing var and printing
    while counter:
        time.sleep(delay)
        threadLock.acquire()
        print ("%s: %s" % (threadName, counter))
        counter -= 1
    threadLock.release()
    threadLock.release()
    threadLock.release()
    
class myThread_ (threading.Thread):    
    def _init_(self, name_, counter,delay):
        # initi thread ,name ,counter and delay.
        threading.Thread._init_(self)
        self.name = name_
        self.counter = counter
        self.delay = delay
    def run_(self):# this is method run
        
        # Get lock to synchronize printing
        #threadLock.acquire()
        print_time_(self.name, self.counter, self.delay)#calling print_time_ global fun.
        # Free lock to release next thread
        #threadLock.release()
threadLock = threading.RLock()#Re-entrant lock
threads_ = []
# Create new threads
thread1_ = myThread_("Hello from Thread", 1,50)
thread1_.run_()#calling run_ method frm thread _ class
# Start new Threads
thread1_.start()
# Add threads to thread list
threads_.append(thread1_)
# Wait for all threads to complete
for t in threads_:    #iterating over the list threads_
    t.join()
print ("Exiting Main Thread")