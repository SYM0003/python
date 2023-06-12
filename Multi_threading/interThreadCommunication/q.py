import queue
import random,threading,time
q=queue.Queue()
items=[]
def producer():
    while True:
        q.put(random.randint(1,10))
        print(f'Producer producing items')
        time.sleep(2)
        print(f'Producer giving notification to the consumers')
        time.sleep(2)
def consumer():
    while True:
        print(f'Consumer waiting for the notification')
        time.sleep(2)
        print(f'Consumer consuming items {q.get()}')
        time.sleep(2)

t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)
t2.start()
t1.start()
