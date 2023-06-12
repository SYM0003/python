# class Student:
#     # static variable(class level variable)
#     college_name='SWAMI VIVEKANAND COLLEGE OF ENGINEERING'
#     # consturctor 
#     def __init__(self,name,branch,year):
#         self.name=name
#         self.branch=branch
#         self.year=year
#     # instance method(object level method)
#     def get_data(self):
#         print(self.name)
#         print(self.branch)
#         print(self.year)
#         print()
#     #class mehtod decorator
#     @classmethod
#     def get_college(cls):
#         print(cls.college_name)
#     # static method
#     #staticmethod decorator
#     @staticmethod
#     def get_sum(a,b,c)->int:
#         return a+b+c



# uncomment this block if you want to see the use of instance variable

class Test:
    def __init__(self,name,roll_no):
        # declaring instance varible inside the constructor
        # can use self
        self.name=name
        self.roll_no=roll_no

        # accessing the instance variable inside the construcor using the self reffrenc variable
        print("printing the name variable using the construcor itself only->",self.name)
    def new_instance_variable(self,marks):
        # declaring instance varible inside the instance method
        self.marks=marks
        #accessing the instance variable inside the instance method using self reffrence variable
        print("printing the name variable using the instanse method only->",self.name)

    # declaring instance varible inside the class only->NOTE didn't work
    # Test.new_instance_variable='new_instance_variable'


t=Test('shyam',54)
print(t.__dict__)
t.new_instance_variable(265)
print(t.__dict__)
# NOTE ->declaring instance variable outside the class using object reffrence <-NOTE
# can be accessed by the particular object only
t.extra_instance_variable=23
print(t.__dict__)

#accessing the instance variable using object reffrence only
print("accessing the instance variable using object reffrence only")
print(t.name)
