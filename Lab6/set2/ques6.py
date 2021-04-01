import threading, time
def print_time(threadName, delay, counter):# passing var and printing
    while counter:
        time.sleep(delay)
        threadLock.acquire()
        print ("%s: %s" % (threadName, counter))
        counter -= 1
    threadLock.release()
    threadLock.release()
    threadLock.release()
    
class myThread (threading.Thread):    
    def _init_(self, name, counter,delay):
        # initi thread ,name ,counter and delay.
        threading.Thread._init_(self)
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):# this is method run
        
        # Get lock to synchronize printing
        #threadLock.acquire()
        print_time(self.name, self.counter, self.delay)#calling print_time global fun.
        # Free lock to release next thread
        #threadLock.release()
threadLock = threading.RLock()#Re-entrant lock
threads = []
# Create new threads
thread1 = myThread("Hello from Thread", 1,50)
thread1.run()#calling run method frm thread  class
# Start new Threads
thread1.start()
# Add threads to thread list
threads.append(thread1)
# Wait for all threads to complete
for t in threads:    #iterating over the list threads
    t.join()
print ("Exiting Main Thread")