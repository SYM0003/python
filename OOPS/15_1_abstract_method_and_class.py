# # abstract method: a method which has no implimentation  
# # or partial imlimentation and only have declaration is
# # called abstract method

# # the implimetation of the method is provided by the child class
# # it is compulson for the child class. if child class has no impli-
# # mentation of the absract method then instnsiation (object creation) is not 
# # possible for child class



# # abstract class: a class which has incomleter implimentation such type of 
# # classes are called abstract class,each abstract class is a child of ABC
# # class,that is present in abc module.



# block1 abstract mehtod
from abc import abstractmethod,ABC
# class Parent:
#     # @staticmethod
#     @abstractmethod 
#     def m1(self):
#         print('This is a method abstract method and will be implimented by the child class')
#         pass
# t=Parent()
# t.m1()


# # block2 abstract CLASS
# from abc import abstractmethod,ABC
# class Parent(ABC):
#     @staticmethod
#     @abstractmethod 
#     def m1():
#         print('This is a method abstract method and will be implimented by the child class')
#         pass
# t=Parent()
# t.m1()


# # EXMAPLE1
# from abc import abstractmethod,ABC
# # class Vehicle(ABC):
# class Vehicle:
#     def __init__(self,Model,Type):
#         self.Model=Model
#         self.Type=Type
#     @abstractmethod
#     def use(self):
#         pass
#     @abstractmethod
#     def tyre(self):
#         pass
# v=Vehicle("Model", "Type")
# v.use()
# v.tyre()
# class Bus(Vehicle):
#     def use(self):
#         print('Used as pasenger vehicle')
#     def tyre(self):
#         print('Basically it has 4 to 6 tyre')

# b=Bus('BMW', 'Buśs')
# b.use()
# b.tyre()

    
