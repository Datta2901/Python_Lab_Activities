import threading, time
def print_time_361(threadName, delay, counter):# passing var and printing
    while counter:
        time.sleep(delay)
        threadLock.acquire()
        print ("%s: %s" % (threadName, counter))
        counter -= 1
    threadLock.release()
    threadLock.release()
    threadLock.release()
    
class myThread_361 (threading.Thread):
    
    def _init_(self, name_361, counter,delay):
        # initi thread ,name ,counter and delay.
        threading.Thread._init_(self)
        self.name = name_361
        self.counter = counter
        self.delay = delay
    def run_361(self):# this is method run
        
        # Get lock to synchronize printing
        #threadLock.acquire()
        print_time_361(self.name, self.counter, self.delay)#calling print_time_361 global fun.
        # Free lock to release next thread
        #threadLock.release()
threadLock = threading.RLock()#Re-entrant lock
threads_361 = []
# Create new threads
thread1_361 = myThread_361("Hello from Thread", 1,50)
thread1_361.run_361()#calling run_361 method frm thread _361 class
# Start new Threads
thread1_361.start()
# Add threads to thread list
threads_361.append(thread1_361)
# Wait for all threads to complete
for t in threads_361:    #iterating over the list threads_361
    t.join()
print ("Exiting Main Thread")