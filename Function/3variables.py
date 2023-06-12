# global and local variable
# global variable: variable declared outside of the function
# local variable: variable declared inside of the functionn


# i.e

a=4#global variable
def display1():
    b=2 #local variable for display1()
    print(b)
    print(a)
def display2():

    # print(b)#won't print will give error
    print(a)
def display3():
    print(a)
# all will print the value of a =4
display1()
display2()
display3()


