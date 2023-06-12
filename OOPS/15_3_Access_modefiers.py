# The member of a class can be accessed from any place in 
# python that reduce the securiy factor of the software

# as other language python also support for access modefiers/specefierss
# there are three types of access specefiers

# public -> by default every memeber is public
    # can be accessed from any where in the program using the reffrence
# private-> declared using two underscore
    # expamle
    # __s=2#-> private variable
    # def __method()-> private method

        #  can be accessed only with in the class
# block 1
# class Test:
#     x=3#public
#     __y=2#private

#     def m1(self):
#         print('this is public method')
#     def __m2(self):
#         print('this is private method')


# t=Test()
# print(t.x)#valid
# # print(t.__x)#invalid->AttributeError: 'Test' object has no attribute 'm1'
# t.m1()#valid
# t.__m2()#invalid->AttributeError: 'Test' object has no attribute 'm1'








# # name mangling concept in python: as we know that we can't access
# # the private member from outside of the class but there is twist if 
# # you a know a secret if python imlimentation than you can access them 
# # from any where in the program, because of these mangling concept python
# # is considered as quiet less secure language as compare to other programing
# # language i will keep it secret so may think a bit about it when ever you come 
# # and read this block of code,bt i'm leaving a hint over here so you may not 
# # frustrate
# # 
# # create an class and there create a private member, now create object of that class
# # now print the __dict__. clue is hidden in the __dict__
# # 
# # 

# class Test:
#     def __init__(self):
#         self.__x=3
# t=Test()
# print(t.__dict__)



# # protected access specefiers-> not available in python
# # variable that can be accessed by the class member and the members of the child class only is called protected specifiers

# # but there naming convention in python for protecte access specefiers
# # if we put one uder score before the name of the variable it is considered as protected access specefiers 

# # exmaple
# class Test:
#     def __init__(self):
#         self._x=3
# t=Test()
# print(t._x)#-> it is protected but still accessible from outside of the class because it not implimented in python
#            #it is just a convention
# print(t.__dict__)





# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# # data hiding concept 
# # in programing we should not allow every one to access our data, so preventing our private 
# # data from outside pepole is known as data hiding concept, we can  acheive this with the 
# # help of private access specifiers

# # exmaple

# # suppose you don't have data hiding concept
# # so i can access my private data from outside of the class also which is not good programing practice

# class Bank:
#     def __init__(self,balance):
#         self.balance=balance

# b=Bank(34253)
# print(b.balance)


# # but what if we have the private access specifiers, so what we can impliment 
# # some authantication process to show the data
# class Bank:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_balance(self):
#         name=input('Enter your username')
#         pas=input('Enter your password')
#         if name==true and pas ==True:
#             return self.__balance

# b=Bank(34253)
# print(b.get_balance())

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# abstraction:
# The concept of highliting the set of services that our software or program is providing and 
# hiding the internal implimentation is called abstraction

# we can acheive this by using the API(APPLICATION PROGRAMING INTERFACE) like django rest API framework and many more

    # advantages  
    # securit,easy enhansment and maintanance


# encapsulation:
# grouping of similar data and corosponding behaiviour of that data is called encapsulation

# a component (class) that follows data hiding and abstraction is called encapsulated componenet
 
