
# good programing practices for Lock
# 1.> always write of releasing the Lock inside the finally block only, the advantage of this
# if we any exception raised after acquiring the Lock then the thread will not able to release the
# Lock if there is no excpetion block for corosponding excpetion and it will be misuse of the resorces


# # 2.> always acquire the Lock using with statement
# import threading
# lock=threading.Lock()
# with lock:
#     pass

# the advantage of the with statement is the lock will be released automatically once the corosponding action
# performed and one more advantage is that if there is excpetion inside the with block then also the lock will
# be released automatically

# Q.what is the advantage of with statement to acquire Lock in multithreading