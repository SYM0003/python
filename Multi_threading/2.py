# METHODS RELATED TO THREADING


import threading,time
def display1():
    time.sleep(10)
    for i in range(5):
        pass
        # print(f'hi shyam this is display1 function')
        # print(f'current thread name is : {threading.current_thread().name}')
        # print(f'current thread id is :{threading.current_thread().ident}')
    print(f'{threading.current_thread().name} thread is compleated')
def display2():
    time.sleep(5)
    print(f'{threading.current_thread().name} is waiting for complition of {t1.name} thread')
    t1.join()
    for i in range(10):
        pass
        # print(f'hi shyam this is display2 function')
        # print(f'current thread name is : {threading.current_thread().name}')
        # print(f'current thread id is :{threading.current_thread().ident}')
    print(f'{threading.current_thread().name} thread is compleated')
# know thread identity
# property/variable name: ident-> pvm gives an identity no to each thread we can access it with this
print(threading.current_thread().ident)
x=5
# check the total no of thread in the program
t1=threading.Thread(target=display1,name='display1')
t2=threading.Thread(target=display2,name='display2')
t1.start()
t2.start()
print(f'active thread count is : {threading.active_count()}')

# to get the list of active threads
l=threading.enumerate()
print(f'list of active threads : {l}')

for thread in l:
    print(thread)
for thread in l:
    print(thread)

# to check the activeness of a thread alive/or not
for thread in l:
    print(f'{thread.name} alive status : {thread.is_alive()}')

print(f'')

# join method
    # join(self, timeout=None)
    #  |      Wait until the thread terminates.
    #  |      
    #  |      This blocks the calling thread until the thread whose join() method is
    #  |      called terminates -- either normally or through an unhandled exception
    #  |      or until the optional timeout occurs.
    #  |      
    #  |      When the timeout argument is present and not None, it should be a
    #  |      floating point number specifying a timeout for the operation in seconds
    #  |      (or fractions thereof). As join() always returns None, you must call
    #  |      is_alive() after join() to decide whether a timeout happened -- if the
    #  |      thread is still alive, the join() call timed out.
    #  |      
    #  |      When the timeout argument is not present or None, the operation will
    #  |      block until the thread terminates.
    #  |      
    #  |      A thread can be join()ed many times.
    #  |      
    #  |      join() raises a RuntimeError if an attempt is made to join the current
    #  |      thread as that would cause a deadlock. It is also an error to join() a
    #  |      thread before it has been started and attempts to do so raises the same
    #  |      exception.

print(f'main thead is waiting for complition of display2')
t2.join()
print(f'{threading.current_thread().name} thread is compleated')

# you can pass timeout to join:
    # the join method will wait for the particular thread unitll it's complition or for timout time
    # after timeout time it will not wait for it.
