''' super function is a function for calling parent class member
in a child class'''
''' it is basically used to remove the naming ambiguity in python'''
''' not required in day to day life'''


#super()->always call member of imidiate parent only if that parent doesn't
# contain that method than pvm will search it in  the parent of that clas
# code 1
# how to call member of a parent class

# class P:
#     def __init__(self,a,b):
#         print("Parent class constructor")
#         self.a=a
#         self.b=b

# class C(P):
#     def __init__(self,a,b,c,d):
#         print("child class constructor")
#         super().__init__(a,b)
#         self.c=c
#         self.d=d
# c=C(1,2,3,4)

# block 2
class A:
    def __init__(self):
        print('A class constructor')
        self.a=3
    def m1(self):
        self.b=3
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    pass
    # def m1(self):
    #     print('C class method')
class D(C):
    def m1(self):
        print('D class method')
        super().m1()

# code 1
# d=D()
# d.m1()


# code 2
# how to call the member of particular parent class inside a child class
# therer are two ways in which we can fullfilll this requirement
# one is shown below 
# syntax:
# class_name.member(self)
# # class E(D):
# class E():

#     # here E is grand child class of class A so we are using the 
#     # shown syntax over here to fulfill our requirement
#     def m1(self):
#         print('E class method')
#         A.m1(self)
#         # what if A was not super parent or parent of E?
# e=E()
# e.m1()
# print(e.__dict__)

# code 3
# second way is by using the super function
# syntax

#         1 super(c,self,other arg)->super call of class c for the current obj
#         2 super(parent_class_name,parent_class_name.member(self))

# class F():
#     def __init__(self):
#         pass
#     def m1(self):
#         print('F class method')
#         super().m1()#will give attribute error has no attribut m1
# f=F()
# f.m1()

# # code3
# class F(D):
#     def __init__(self):
#         pass
#     def m1(self):
#         print('F class method')
#         super().m1()#will give attribute error has no attribut m1
# f=F()
# f.m1()





# code 3 
class F(D):
    def __init__(self):
        pass

    def m1(self):
        print('F class method')
        super(D, self).m1()

f=F()
f.m1()