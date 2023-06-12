# # syntax: 
# # def function_name(arg1,arg2):
# #     body
# def sum1(a,b):
#     '''give two perameter'''
#     return a+b

# print(sum1(10,5))
# print(sum1(10,8))
# print(sum1(10,2))
# print(sum1(10,6))
# sum1()






# # types:
# # 1.built in function
# # 2.user defined function
 
# #  wap for factorial of given no
# def factorial(a):#a is peramerter
#     if a==1:
#         return a
#     return a*factorial(a-1)
# print(factorial(3))#3 is argument
# print(factorial(6))
# print(factorial(2))


# # types of argument or perameter
# # 1. positional argument
# # this are only normal arguments i.e
# def sum(a,b):return a+b
# sum(3,5)#passing the arg in this fashion is positional argument

# # 2. keyword arg
# sum(a=3, b=2)

#     # NOTE we can use both positional and keyword agr simultaniously
# sum(3,b=2)#valid
#     # NOTE but keyword arg take place only after positiona arg
# # sum(a=3,3)#invaid
# # 3. default argument

# # syntax
# # def function_name(arg='default'):body-->valid
# # def function_name(arg1,arg2='default'):body-->valid

#     # note: default argument should only define after non_default argument
# # def function_name(arg1='default',arg2):
# #     print('body-->invalid')


# # 4. variable length arg
# # we can pass any number of argument to the function with the help of variable length arg
# # syntax

# # def fun(*x):
#     # type of x is tuple we can use x as tuple
# #     #body


# # i.e.
# def sum1(*x):
#     t=0
#     for a in x:
#         t=t+a
#     return t


# print(sum1(1,3))
# print(sum1(1,3,5))
# print(sum1())




# # NOTE we can pass variable length peramenter
# # with normal argument,but after variable length arg if we are calling any arg then
# # we must call it by keyword argument only

# # i.e
# def fun(*x,y):
#     print(x)
#     print(y)
# # fun(1,3,5,5,7,2)#invalid
# fun(1,35,542,2,6,2,y=6)#valid

# NOTE : 
# 1 we can't take multiple variable length arg in a single function
# 2 we can take defalut arg befor variable length arg,but not before normal arg


# *args->any no.of argument
# **kwargs-> any no of key value pair args

i.e