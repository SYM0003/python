import threading
import time
import random


# example 1 traffic signal


def police():
    while True:
        print("police giving red signal")
        e.clear()
        time.sleep(10)
        print("police giving green signal")
        e.set()
        time.sleep(20)


def vehicles():
    while True:
        print('Vehicles are waiting for green signal')
        e.wait()
        print('Got green signal vehicles are crossing the road')
        cnt=0
        while(e.is_set()):
            time.sleep(2)
            cnt=cnt+random.randint(0,10)   
        print(f'Total {cnt} vehicle passed')  
        
t1=threading.Thread(target=police)
t2=threading.Thread(target=vehicles)
e=threading.Event()

t1.start()
t2.start()