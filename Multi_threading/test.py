# from threading import *
# import time
# def display1():
#     print('display1 function')
#     print(f'Current thread is : {current_thread().name}')
#     time.sleep(10)
#     # t2.start()
# def display2():
#     print('display2 function')
#     print(f'Current thread is : {current_thread().name}')
#     time.sleep(15)
#     # t3.start()
# def display3():
#     time.sleep(20)
#     print('display3 function')
#     print(f'Current thread is : {current_thread().name}')
#     # t1.start()





# t1=Thread(target=display1)
# t2=Thread(target=display2)
# t3=Thread(target=display3)

# t1.start()
# t2.start()
# t3.start()


import threading

t=threading.Thread(target=print,args=('this is new thread',),name='print')
print(t.daemon)
# print(t.isDaemon())
print(t.ident)
print(t.native_id)
print(t.is_alive())
print(t.run())