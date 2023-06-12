'''program to demonastrate is a relation(inharitance)'''

# # as we know that we can access the member of one class inside 
# # other class 
# # there are two ways for this 
# # one is has a relation(create a object of one class and pass that variable to the second class)
# # second is is a relation (inharitance)

# # syntax:
# # class child(parent):
#     # pass


# # example one

# class Parent:
#     def __init__(self,a):
#         self.a=a
#         print("Parent class constructor") 
#     def m1(self):
#         print('method of Parent class')
#     @classmethod
#     def m2(cls):
#         print('classmethod of Parent class')
#     @staticmethod
#     def m3():
#         print('static method of Parent class')

# class child(Parent):
#     # here we are using the concept of the inhartance
#     # the child class can access the member of the Parent class 
#     # it means when ever we will create the object of the Child class
#     # then we with the help of that object we access the member and mehtod of Parent 
#     # class as well as member of the child class
#     pass

# c=child(2)
# child.m2()#->accessing the classmethod of Parent class using obj of child class
# child.m3()#->accessing the static method of Parent class using obj of Child class

# # NOTE that if the child class will have it's own constructor than the constructor of 
# # child class will be executed when we will create the obj of child class and if will not
# # have any constructor than only parent class constructor will be executed







# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # super() function
# # super() function can be used to call parent class functionality


# # importance of inharitance 
# # code reusability
# 
# # NOTE NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # has a v/s is a
# # if we want to extend exiting functionality with some more functionality
# # than we should go for is a (employee and person)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eatanddring(self):
#         print('Do nothing except eating and drinking')
# class Employee(Person):
#     # here we are extendin the functionality of Person class and also
#     # using the existing functionalitis
#     def __init__(self,name,age,esal,eno):
#         super().__init__(name,age)
#         self.esal=esal
#         self.eno=eno
#     def work(self):
#         print(f'{self.name} do nothing except taking salary of {self.esal}')

# emp=Employee('Vishal', 23, 230000, 523222)
# emp.eatanddring()
# emp.work()

# #  NOTE NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# if we don't want to exted and we just want to use existing functionality
# than we should go for has a (employee and carr)



# # i.e

# class Car:
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def getinfo(self):
#         print(f'\tName: {self.name}\n\tMOdel: {self.model}\n\tColor {self.color}')
    

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eatanddring(self):
#         print('Eating Biryani and Beer')

# class Employee(Person):
#     def __init__(self,name,age,eno,esal,car):
#         super().__init__(name, age)#calling parent class constructor
#         self.eno=eno
#         self.esal=esal
#         self.car=car
#     def work(self):
#         print('Work info:')
#         print('\tPython devoleper')

#     def empinfo(self):
#         print(f'Employee name: {self.name}')
#         print(f'Employee age: {self.age}')
#         print(f'Employee eno: {self.eno}')
#         print(f'Employee esal: {self.esal}')
#         print(f'Employee car info:')
#         self.car.getinfo()


# car=Car('BMW', '2.3', 'Black')
# emp=Employee('Shyam', '23', 23214, 45000, car)
# emp.empinfo()
# emp.work()
# emp.eatanddring()#accessing the paret class method
        
