from threading import *
import random
import time

queue = []
MAX_SIZE = 3
condition = Condition()

class Producer(Thread):
    def run(self):
        while True:
            condition.acquire()
            if len(queue) == MAX_SIZE:
                print('Buffer is full, producer is waiting')
                condition.wait()
                print('Producer resuming')
            num = random.randint(0,11)
            queue.append(num)
            print(f'Produced {num}')
            condition.notify()
            condition.release()
            time.sleep(1)

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print('Nothing in queue, consumer is waiting')
                condition.wait()
                print('Consumer Resumed')
            num = queue.pop(0)
            print(f'Consumed {num}')
            condition.notify()
            condition.release()
            time.sleep(2)

Producer().start()
Consumer().start()