'''
    synchronization: means allowing only one thread to use the resources of the system at
                    particular time. 
    
    synchronization using Lock()
        Lock is  simplest mechanism for synchronization
    synchronization using RLock()
        RLock is  updated version of Lock  for synchronization
            there were some limitation in Lock mechansism of syncrhonization
            Lock doesn't take care of the owner,means it doesn't know that which 
            thread is currently accured the lock(or critical code)
            
            so if the critical code is accured by any thread and now any thread
            want to accure that code than it will not allow to that thread not 
            even to the owner of the critcal thread.

            so it becoms useless in recursive and nested function where a function
            may need to accure the critical code multiple time without realisng the 
            critical code

            this draback is removed by RLock()->renentrance lock
            it is similar to Lock just with one diffrence that it stores the info about 
            the owner thread.
            so that it can give access to the owner thread for multiple times


    synchronization using Semaphore()
        semaphore is the most advanced mechanism for synchronization
        the Lock and RLock mechansim have the drawback that at a time only one 
        thread can access the critical code but some time we may need such a 
        mechanism that emphasize to allow multiple limited thread that can use 
        the critical code.
        for an example we can thin about a database connection system where at 
        a time at most 10 connection can be established so in this scenario our
        Lock and RLock mechansim may not able to provide such flexibilty to the 
        programer and here comes the role of Semaphore()
'''


import threading,time
l=threading.Lock()
r=threading.RLock()
s=threading.Semaphore(2)
bs=threading.BoundedSemaphore(2)
result=1
def fib(n):
    r.acquire()
    if n==0:
        result=1
    else:
        result=n*fib(n-1)
    r.release()
    return result
def display(name)->None:
    for i in range(10):
        r.acquire()
        print('hello',end=' ')
        time.sleep(2)
        print(name)
        r.release()
def display1(name)->None:
    for i in range(10):
        print(s._value)
        # s.acquire()
        s.acquire()
        s.acquire()
        print('hello',end=' ')
        time.sleep(2)
        print(name)
        s.release()
        s.release()
        s.release()
def display2(name)->None:
    for i in range(10):
        print(s._value)
        # s.acquire()
        bs.acquire()
        bs.acquire()
        print('hello',end=' ')
        time.sleep(2)
        print(name)
        bs.release()
        bs.release()
        # # if we will release the Semaphore that is not accuired by that thread 
        # # than we will get the ValueError: ValueError: Semaphore released too many times
        # bs.release()
        # bs.release()
        # bs.release()
def main()->None:  
    # # code for showing how does Lock work?  
    # t1=threading.Thread(target=display,args=('shyam',),name='shyam_thread')
    # t2=threading.Thread(target=display,args=('vishal',),name='vishal_thread')
    # t3=threading.Thread(target=display,args=('shubham',),name='shubham_thread')
    # t1.start()
    # t2.start()
    # t3.start()

    # # code for showing how does RLock work?
    # t1=threading.Thread(target=print,args=(fib(5),))
    # t2=threading.Thread(target=print,args=(fib(9),))
    # t1.start()
    # t2.start()

    # # code for showing how Semaphore works?
    # t1=threading.Thread(target=display1,args=("shyam",),name="shyam_thread")
    # t2=threading.Thread(target=display1,args=("Sumit",))
    # t3=threading.Thread(target=display1,args=("Shubham",))
    # t4=threading.Thread(target=display1,args=("Vishal",))
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()


    # code for showing how BoundedSemaphore works?
    # code for showing how Semaphore works?
    t1=threading.Thread(target=display2,args=("shyam",),name="shyam_thread")
    t2=threading.Thread(target=display2,args=("Sumit",))
    t3=threading.Thread(target=display2,args=("Shubham",))
    t4=threading.Thread(target=display2,args=("Vishal",))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    

main()
