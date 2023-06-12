

# # ex1

# try:
#     print("try block")
# except:
#     print('exception block')

# finally:
#     print("finally block")


# # o/p:
# # try block
# # finally block


# # ex2:
# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)
# finally :
#     print("Cleanup activity")

# # division by zero
# # Cleanup activity


# # ex3 finally vs return 

# def fun():
#     try:
#         return 9
#     except:
#         print('exception')
#     finally:
#         return 7

# import os # didn't get NOTE
# def fun2():
#     try:
#         os._exit()
#     except:
#         return 1
#     finally:
#         return 5
# def fun3():
#     print(10/0)
#     try:
#         return 0
#     except:
#         return 1
#     finally:
#         return 2
# print(fun())
# print(fun2())
# print(fun3())





# # nested try,except,finally
# try:
#     print('st1')
#     try:
#         print('st5')
#     except ZeroDivisionError:
#         print('st6')
#     finally:
#         print('st7')
# except NameError:
#     print('st2')

# finally:
#     print('st3')
# print('st4')



# # flow analysis
# try:
#     st1
#     st2
#     try:
#         st3
#     except:
#         st4
#     finally:
#         st5
#     st6
#     st7
# except abc:
#     st8
# finally:
#     st9
# st10


# case 1 no exception: 1,2,3,5,6,7,9,10,at
# case 2 exception at st2 and exception matched: 1,8,9,10,nt
# case 3 exception at st2 and exception did not match: 1,9,at
# case 4 exception at st3 and inner exception matched: 1,2,4,5,6,7,9,nt
# case 5 exception at st3 and inner exception didn't match but outer excepion block matched: 1,2,5,8,9,10 no
# case 6 exception at st3 and both excepion block didn't match: 1,2,5,9,at
# case 7 exception at st4 and  excepion block matched: 1,2,5,8,9,10 nt
# case 8 exception at st4 and  excepion block didn't match: 1,2,5,9 at
# case 9 exception at st5 and excpetion block matched : 1,2,,,8,9,10 nt
# case 10 exception at st5 and excpetion block didn't match : 1,2,,,9 at
# case 11 exception at st6 and excpetion block matched : 1,2,,,,5,8,9,10nt
# case 12 exception at st8 : ,,,,,,,9 at
# case 13 exception at st9: ,,,,,,,, at
# case 14 exception at st10: ,,,,,,,,, at



# ----------------------------------------------------

# try-except-else-finally

# else block: when write a block of code in try block and if there is know excpetion
# in it then else block will be executed or if excpetion raised then then except block will be executed
# but with will never executed simultaneously.

# try:
#     print('a')
#     print(a)
# except NameError:
#     print('st2')
# else:
#     print('else block')
# finally:
#     print('st3')
# print('st4')



# conclusion
# 1) Whenever we are writing try block, compulsory we should write except or finally 
# block.i.e without except or finally block we cannot write try block.
# 2) Wheneever we are writing except block, compulsory we should write try block. i.e 
# except without try is always invalid.
# 3) Whenever we are writing finally block, compulsory we should write try block. i.e 
# finally without try is always invalid.
# 4) We can write multiple except blocks for the same try,but we cannot write multiple 
# finally blocks for the same try
# 5) Whenever we are writing else block compulsory except block should be there. i.e 
# without except we cannot write else block.
# 6) In try-except-else-finally order is important.
# 7) We can define try-except-else-finally inside try, except, else and finally blocks. i.e 
# nesting of try-except-else-finally is always possible






