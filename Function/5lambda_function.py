# # lambda function or anonymous function
# # a function without name is called lambda function

# # lambda function for sum of 2 no
# s=lambda a,b:a+b
# print(s(1,3))#4
# print(s(25,16))#41



# # use of lambda function

# # 1.passing function as argument
# # filter(function,sequence)->filters values present in the sequence based on the condition of function
# # i.e
# # using normal function
# def is_even(n):
#     if(n%2==0):
#         return True
#     return False
# op=list(filter(is_even,[1,35,56,3,2,6,335]))
# print(op)
# # using lambda function
# # op1=list(filter(lambda n:True if n%2==0 else False,[1,35,56,3,2,6,335]))
# # optional of line 24 NOTE
# op1=list(filter(lambda n:n%2==0,[1,35,56,3,2,6,335]))
# print(op1)


# # wap for filtering the string which has len greater than 4
# ans=list(filter(lambda n:len(n)>5, ['sfhsdf','abv','afb']))
# print(ans)


# # wap demonastrating use of lambda function

# class Employee:
#     def __init__(self,name,sal,age,hasgf):
#         self.name=name
#         self.sal=sal   
#         self.age=age
#         self.hasgf=hasgf
#     def display(self):
#         print(self.name)

# e1=Employee("vishal", 23435, 19, True)
# e2=Employee("shubham", 30000, 21, False)
# e3=Employee("shyam", 1000000, 21, True)
# ans=filter(lambda e:e.sal>25000 and e.age>20 and e.hasgf==True, [e1,e2,e3])
# for e in ans:
#     e.display()


# # map(func, iter1)--> returns equivalent value for each x in iter1 based on operation of funct

# l=[1,2,6,7,4,3,8,71,]
# def fun1(n):
#     n=0
# m=list(map(lambda n:n**2,l))
# print(m)

# # wap for multiplying the element of l1 and l2
# l1=[1,3,4,6,3,7,8]
# l2=[10,20,30,40]
# output=list(map(lambda x,y:x*y,l1,l2))
# print(output) #[10, 60, 120, 240]



# # reduce()->returns a single value for the given sequenc by performing operation based on function
l2=[10,20,30,40]
from functools import *
# reduce(
# , sequence, initial)
output=reduce(lambda x,y:x+y, l2, 0)
print(output)#100

 
