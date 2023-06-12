# # try block with single excpet block
# try:
#     print(10/0)
# # except ZeroDivisionError as e:
# except BaseException as e:
#     print(e.__class__.__name__)
#     print(type(e))
#     print(type(e).__name__)
#     print(e)



# # try with multiple except block

# try:
#     x=int(input("Enter first number"))
#     y=int(input("Enter second number"))

#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except BaseException: # it can handle any kind of exception
#     print("other error")



# # single except block for multiple excpet block
# try:
#     x=int(input("Enter first number"))
#     y=int(input("Enter second number"))

#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print(e)


# default exception
try:
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))

    print(x/y)
except :
    print("Error")







# finally block






