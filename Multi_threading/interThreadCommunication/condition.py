import threading

def producer():
    c.acquire()
    print(f'Producer producing items')
    print(f'{c._waiters} threads are waiting')
    c.notify(1)
    print(f'Producer giving notification to the consumers')
    c.release()
def consumer():
    c.acquire()
    print(f'Consumer waiting for the notification')
    c.wait(10)
    print(f'Consumer consuming items')
    c.release()
    pass


c=threading.Condition()
t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)

t2.start()
t1.start()
