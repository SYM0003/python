# # multi threading without creating any class
# import threading
# def display():
#     for i in range(10):
#         print('shyam')

# # th=threading.Thread(target=display,args=())
# th=threading.Thread(target=display)
# th.start()
# for i in range(10):
#     print('vishal')




# # # multi threading by exteding the thread class of threading module
# from threading import *

# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print(f'good morning shyam')


# th=MyThread()
# th.start()
# for i in range(5):
#     print(f'good morning vishal')




# # multi threading without exting the thread class
# from threading import *
# import time
# class MyClass:
#     @staticmethod
#     def display(name):
#         for i in range(5):
#             time.sleep(1)
#             print(f'hello {name}')


# th=Thread(target=MyClass.display,args=('shyam',))
# th.start()
# for i in range(5):
#     time.sleep(1)
#     print(f'hello vishal')




# getting and setting the name of thread:
# in python each thread is asigned a name by the pvm
# if want to change that name so we can do it using 
# the method of threading module named setname()


from threading import *
# note: getName and setName methods of Thread class are deprecated now we shoud use name variable for
# same requirements
print(f'{current_thread().name} is started executing')
def display():
    current_thread().name='display'
    print(f'{current_thread().name} thread is started executing')
    for i in range(10):
        print('shyam')

# th=threading.Thread(target=display,args=())
th=Thread(target=display)
th.start()
for i in range(10):
    print('vishal')












# # ex2: suppose i've two list l1 and l2 and
# # and i want to find sum of l1 as well as sum of l2
# # so these two process are independent in there selves
# # therfore we shoud use multithreading over here to improve 
# # perofrmance of the program
# import time,threading
# l1=[x for x in range(10)]
# l2=[x for x in range(10)]

# def suml(l1):
#     sum=0
#     for i in l1:
#         time.sleep(1)
#         sum+=i
#     # print(sum)

# # tradition way: 20.01634907722473
# t1=time.time()
# suml(l1)
# suml(l2)
# print(f'time taken by traditonal way : {time.time()-t1}')

# # using multithreading 10.012078523635864
# th1=threading.Thread(target=suml,args=(l1,))
# th2=threading.Thread(target=suml,args=(l2,))
# t1=time.time()
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print(f'time taken by multithreading way : {time.time()-t1}')
