import threading,time
def display():
    time.sleep(5)
    print('this is supporting thread/daemon thread')
    print(f'daemon nature of {threading.current_thread().name} is : {threading.current_thread().daemon}')
        # the daemon nature of current thread will depend on the nature of the thread where from it is started
        # since i'll start it from main thread so it will give false(line 60)
    time.sleep(5)
    print('thread terminated succefully')


# # daeomon thread: daemon thread can be define as a thread which run in background.
# # the objective of daemon thread is to provide support for non daeomon thread.
# # garbage collector is also a daemon thread.

# # how to check the demon nature of a thread
#     # there is a property(variable) of Thread object daemon which gives True/false for daemon/nondamemon
#     # in earlier version there was  a method isaemon() with same purpose but it is depricated now
# print(threading.current_thread().daemon)


# # how to change the daemon nature of a thread
# # you can change the nature by setting daemon as True or False

# # but there is a catch
# # as we know each program is ran by main thread so we it means there will be atleast one thread in 
# # each program by default so the quetions is can we change the daemon nature of main thread?
# # and ans is no! we can not change the daemon nature of main thread :
# # the reason behind it is we can change the daemon nature of a thread only before starting 
# # the thread once the thread is started we can't change the daemon nature of any thread
# # and the main thread get started once the program is started therfore we can't change the 
# # daemon nature of main thread or any thread that has been already started.

# # threading.current_thread().daemon=True
#     # RuntimeError: cannot set daemon status of active thread
# # we  can use threading.current_thread().setDaemon() in earlier version for it but in newer version it is
# # depricated


# # let's create a thread
# t1=threading.Thread(target=print,args=('This is empty thread',),name='null thread1',daemon=True)
# # i've decided the daemon nature of thread 't1' at it's defination only
# # but we can do it explicitly also


# t2=threading.Thread(target=print,args=('This is also empty thread',),name='null thread2')
# t2.daemon=True


# print(f'daemon nature of {threading.current_thread().name} is {threading.current_thread().daemon}')
# print(f'daemon nature of {t1.name} is {t1.daemon}')
# print(f'daemon nature of {t2.name} is {t2.daemon}')



# # daemon nature of a thread is inharited from it's parent thread if we do not define it anywhere

# # the parent of thread is defined by the place where the particular thread was started(in which tread)

# t3=threading.Thread(target=display,name='display')
# # if start thread 't3' here then 'main tread' will be the parent thread of 't3'.
# print(f'daemon nature of {threading.current_thread().name} is {threading.current_thread().daemon}')
# t3.start()










# the daemon thread get terminated automatically once all non daemon thread are terminated without executing 
# remaining content

# daemon thread
def display1():
    print('i am daemon thread for supporting purpose')
    for i in range(10):
        print(f'exucting {threading.current_thread().name}')
        pass

dm=threading.Thread(target=display1,name='daemon',daemon=True)

'''
    in this block of code as dm is a daemon thread and will be in running/executing cond
    till there is atleast one one daemon thread in running/executing cond.
    if dm is executed completely then it must print the statement for 10 times if it is not
    able to print that then it is sure that there is no more non daemon thread in running cond
    that's why the daemon thread also get termintated
'''
dm.start()
# time.sleep(20)
print(f'executing {threading.current_thread().name}')