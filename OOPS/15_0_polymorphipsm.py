''' polymorphism demonstration'''
''' polymorphism is a characterstics of objects of showing 
    diffrent diffrent behaviour in diffrent diffrent situationns
'''

'''
Polymorphism:
    overloading
        operator overloading
        method overloading
        constructor overloading
    overriding
        method overriding
        constructor overriding
'''


# # --------------------------------------------------------------------
# # operator overloading
#     # suppose i have a book class and it has two instances name and pages
#     # with the help of the book class i created two book object. now i want to 
#     # find the sum of the pages of both book how can do it? one way is by using
#     # object reffrences as shown in block 1(below code):

# class Book:
#     def __init__(self,name,pages):
#         self.name=name
#         self.pages=pages

# b1=Book('Rich Dad Poor Dad',299)
# b2=Book('Atomic Habit',458)

# print(f'Total pages={b1.pages+b2.pages}')



# # what if i can do it with this block?
# # print(b1+b2)
# # we can bring this kind of flexibility in our code by using the operator overloading concept
# # i have added a method in the above Book class check it
# '''
# i have added the __add__() method in the class
# it is default method in python for '+' operator overloading
# we can change the functionality of the operator according to our bussiness requiremnt
# '''
# # block 2
# class Book:
#     def __init__(self,name,pages):
#         self.name=name
#         self.pages=pages
    
#     def __add__(self,other):
#         return self.pages+other.pages

# b1=Book('Rich Dad Poor Dad',299)
# b2=Book('Atomic Habit',458)
# print(f'total no of pages {b1+b2}')




# # block 3 '*' operator overloading
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self,other):
#         return self.salary*other.day
# class TimeSheet:
#     def __init__(self,name,day):
#         self.name=name
#         self.day=day
#     def __mul__(self,other):
#         return other.salary*self.day
# e=Employee('Vishal', 200000)
# t=TimeSheet('Vishal', 20)

# print(f'Total salary {t*e}')




# # --------------------------------------------------------------------
# # block 3 < operator overloading
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def __lt__(self,other):
#         if self.marks==other.marks:
#             return self.name<other.name
#         return self.marks<other.marks
# s1=Student('Shyam', 458)
# s2=Student('Vishal', 458)
# print(s1<s2)


# # --------------------------------------------------------------------
# # block 4 __str__() method
# '''suppose you have a class Book and you created an object b1 of that class
#     now you want to print b1 object than what will happen?

# '''

# class Book:
#     def __init__(self,name,pages):
#         self.name=name 
#         self.pages=pages
# b1=Book("Rich Dad Poor Dad", 299)
# print(b14)#<__main__.Book object at 0x0000027AFC187D60>



# # when ever we do such type of thing the pvm calls the __str__() method of the object 
# # class and that class implimented in such way so that it can return this type of result
# # if we want to change this behaviour than we can impliment it for particular class

# class Book:
#     def __init__(self,name,pages):
#         self.name=name 
#         self.pages=pages
#     def __str__(self):
#         return f'{self.name} has {self.pages} pages'
# b1=Book("Rich Dad Poor Dad", 299)
# print(b1)#Rich Dad Poor Dad has 299


# # block 4 '+' for multiple oprands
# class Book:
#     def __init__(self,name,pages):
#         self.name=name 
#         self.pages=pages
#     def __add__(self,other):
#         total_pages = self.pages+other.pages
#         return Book('New Book',total_pages)
#     # def __str__(self):
#     #     return self.pages
  
# b1=Book("Rich Dad Poor Dad", 299)
# b2=Book("Atomic  Habit", 486)
# b3=Book("How to win frieds", 289)
# print((b1+b2+b3).pages)


# # block 41 '+' for multiple oprands
# class Book:
#     def __init__(self,name,pages):
#         self.name=name 
#         self.pages=pages
#     def __add__(self,other):
#         total_pages = self.pages+other.pages
#         return Book('New Book',total_pages)
#     def __str__(self):
#         return str(self.pages)
  
# b1=Book("Rich Dad Poor Dad", 299)
# b2=Book("Atomic  Habit", 486)
# b3=Book("How to win frieds", 289)

# print(b1+b2+b3)






# # --------------------------------------------------------------------
# # method overloading: when we  define two or more method with same name but diffrent
# # argument than it is called method overloading. Python doesn't support method overloading
# # it is really not required, we can fullfill it without overoading the method

# # method overloading in cpp
# file=f'E:\\shyam\\programing\\c++\\oops\\method_overloading.cpp'

# # There are two types of method overloading:
# # 1 by varing the type of arg
# # 2 by varring the no of arg 

# # as we saw how method overloading works in cpp

# # method overloading is not required in python because there are 
# # some alternative ways already in python so we don't need it in 
# # python;

# # 1st type of overloading is when we pass diffrent type of arg (like int,char,float etc), but in python we
# # can pass any type of arg to a method.


# # 1st type of  method overloading in python

# # block 5 
# class Show_type:
#     @staticmethod
#     def show(arg):
#         print(arg.__class__.__name__)

# Show_type.show(5)#int
# Show_type.show(5.6)#float
# Show_type.show(5+2j)#complex
# Show_type.show('5')#str

# # as you can see that we realy don't need the concept of method overloading for 
# # first type of overloading




# # but what about the second type of method overloading:
# # we can acheive the goal of second type of method overloading 
# # using the default arg and variable length arg

# # block 6
# # achieving method overloading with the help of default arg
# class Total:
#     def total(x=0,y=0,z=0):
#         print(x+y+z)
# Total.total()#0
# Total.total(5)#5
# Total.total(2,5)#7
# Total.total(2,5,4)#11


# # block 7
# # achieving method overloading with the help of variable length arg
# class Total:
#     def total(*arg):
#         print(sum(arg))
# Total.total()#0
# Total.total(5)#5
# Total.total(2,5)#7
# Total.total(2,5,4)#11


# # --------------------------------------------------------------------
# # block 8 constructor overloading 
# # we can acheive the goal of constructor overloading in similar 
# # fashion as we acheived it for method overloading



# class Test:
#     def __init__(self,x=None,y=None,z=None):
#         if x is None and y is None and z is None:
#             print('constructor for zero arg')
#         elif x is not None and y is None and z is None:
#             print('constructor for one arg')
#         elif x is not None and y is not None and z is None:
#             print('constructor for two arg')
#         else:
#             print('constructor for three arg')

# t=Test()
# t=Test(5)
# t=Test(5,4)
# t=Test(1,5,5)

# # --------------------------------------------------------------------
# class Test:
#     def __init__(self,arg):
#         print(f'constructor for {arg.__class__.__name__} type variable')

# t=Test(5)
# t=Test(5.4)
# t=Test(1+5j)
  


# # --------------------------------------------------------------------
# # block 9 overriding:
# # in inharitance the members of parent class are available to the 
# # child class but sometime child class may need to define the same 
# # method in its own fashion so, redifining the method of parent 
# # class method in the child class method is called method overriding


# # EXAMLE:
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def show(self):
#         print(f'Name: {self.name}\nage: {self.age}')


# class Employee(Person):
#     # constructor overriding
#     def __init__(self, name, age,salary,id):
#         super().__init__(name, age)
#         self.salary=salary
#         self.id=id
#     # method overriding
#     def show(self):
#         super().show()
#         print(f'Salary: {self.salary}\nid: {self.id}')



# p=Person('Shyam', 23)
# p.show()
# e=Employee('Rohan', 32, 203402, 330)
# e.show()