# if we want to reprasent a group of object as single entity than we shold go for list data type
# features of list:----
    # in list insertion order is preserved and duplicates are allowed.
    # hetrogenious objects also allowed.
    # It is dynamic in nature


# creation of list object

# # 1.empty list
# l=[]
# # 2.if you know elements already
# l=[1,3,5,6]




# # 3.with dynamic input 
# l=(input("Please enter a list").split())

# l=eval(input("Please enter a list"))

# print(l)
# print(type(l))


# DIFFRENCE BW FUNCTION AND METHODS
    # # METHODS--> OOPS BASED CONCEPT
    # # FUNCTION--> POP BASED CONCEPT

    # def f1():
    #     print('f1 is called')
    # class test:
    #     # METHODS: function which is defined inside the class and associated with that class
    #     def m1(self):#
    #         print('m1 is called')


    # # we call function directly but we can't call the method directly for calling method we must have to 
    # # create the object of the class from where it belongs

    # t=test()
    # t.m1()
    # f1()






# IMPORTANT FUNCTION AND METHODS OF LIST
# l=[1,3,4,5]
# print(len(l))
# print(l.count(3))#-->returns the number of occurence of given value in the list
# print(l.index(1))#-->returns the index of the given value(first occurenc index)
# NOTE NOTE NOTE NOTE NOTE NOTE # NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE # NOTE NOTE NOTE NOTE NOTE NOTE
# if given value is not present in the list then it will give value error
# NOTE NOTE NOTE NOTE NOTE NOTE # NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE # NOTE NOTE NOTE NOTE NOTE NOTE

# HOW TO PREVENT THIS?
# BY USING MEMBERSHIP OPERATOR. IN


# WAP FOR FINDING AN ELEMENT IN THE LIST, TAKE ELEMENT FROM THE USER.

# TO GET INFORAMTION OF LIST
    # len()
    # index()
    # count()

# TO MANUPULATE THE LIST
    # HOW TO ADD ELEMENT IN LIST(HINT THERE ARE three METHOD FOR THE SAME,TELL DIFF BW THEM ALSO )
    # TO ADD ELEEMENT IN THE LIST THERE ARE THREE METHODS IN PYTHON
    # list.append(value)
        #insert a single element at the end of the list value may be of any kind
    # list.insert(index,value)
        #insert element at given index 
    # list.extend()
        #insert multiple values in the list at the end
    # l=[1,3,4,5]
    # print(l)
    # l.append(3)#l=[1,3,4,5,3]
    # print(l)
    # l.insert(2,12)#l=[1,3,12,4,5,3]
    # print(l)
    # l.insert(2,[1,3,4])#l=[1,3,[1,3,4],12,4,5,3]
    # print(l)
    # l.append([1,3,4])#l=[1,3,[1,3,4],12,4,5,3,[1,3,4]]
    # print(l)
    # l.extend([1,3,4])#l=[1,3,[1,3,4],12,4,5,3,1,3,4]
    # print(l) 
    
# how to remove the element from the list?
# l.remove(value);#-->removes the given value from the list(only first occurence)

# how to remove all ocuurence of given value?
    # we can use loop functionality for the same but there is no specific method or function for it.
    # l=[1,3,4,5]
    # i=0;
    # n=len(l)
    # while i<n:
    #     l.pop()
    #     i+=1
    # print(l)



# how to remove element by passing index?
    # therer is method pop() for the same if we don't pass any index than 
    # it will delete the index which is present on last 
    # index and if we pass the idex value which is bigger than length of the 
    # list than we will get the index error
# how to remove all element fromt the list 
# l.pop();
# l.clear()
    # we have clear() mehtod for it. 
        # l.clear()
    # instead of this we can do this 
        # l=[]



    # # WRTIE A PROGRAM TO ADD ELEMENT FROM 1 TO 100 IN A LIST WHICH ARE DIVISABLE BY 10
    # l2=[]
    # count=0
    # for x in range(1,101):
    #     count+=1
    #     if count ==10:
    #         l2.append(x)
    #         count=0
    # print(l2)






# ORDER ELMENT OF THE LIST
# REVERSE
# SORT
# cloning concept
# cloning v/s aliasing
    # l1=[1,3,4,5,2]
    # sr=sorted(l1)
#     # print(sr)
# l=[1,34,2,4,6,32]
# l.reverse()#-->this we reverse the list on the basis of insertion order
# l.sort()#--> it will sort the list on the basis of asending order
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
# WE CAN'T SORT TWO DIFFRENT DATA TYPE (I.E STR AND INT ),IT WILL GIVE ERROR
# IN SORT FUNCITON THERE IS REVERSE ARG WHOSE DEFAULT VALUE IS FALSE
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
# print(l)

# DIFFRENCE BW SORTED AND SORT or reversed and reverse
    # sort is method for list and sorted() is python's default  function which return the sorted object,
    # sort method doesn't return any thing

    # t=1,3,45,4
    # tr=sorted(t)
    # print(t)
    # print(tr)








# ALIASING : CREATING DUPLICATE REFFRENSE VARIABLE FOR EXISTING VARIABLE,
    # ADVANTAGE : WE CAN ACCESS THE OBJECT BY ANY OF THE ALIASED OBJECT.
    # l1=[1,2,3,4,5,6]
    # l2=l1
# CLONING: CREATING DUPLICATE OBJECT AND ASIGNING IT TO NEW REFRENCE VARIABLE.
    # way of cloning?
    # if want to do cloning of any object then we do same by this way:
    # second is by using copy() method.

    # l1=[1,2,3,4,5,6]
    # l2=l1.copy()
    # print(id(l1))#2508185413888
    # print(id(l2))#2508185366912

    # first is by using slice operator[only applicable wher indexing concept can be applied]
    # l3=l1[:]
    # print(id(l1))#2508185413888
    # print(id(l3))#2508185320192



# NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE
# NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE
# WHT IS DIFFRENCE BW THIS TWO CODE OF LINE
# l1=l2
# l1=l2.copy()
# in the first line we creating anoteh reffrence varible to tho object where l1 is pointing, with the 
# help of this variable we can manupulate that object. If we'll access that object either through l1 or either l2 
# will get the same result.
# in the second line we are creating new object wich has same value as l1 but it has it's own existanse.
# where l2 is  list type data structure.
# NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE
# NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE # NOTE NOTE








# Mathematical OPERATOR for list object
# + OPERATOR--> in the case of list if we use + operator than we must use both operands of list type 
#               if won't do this than we'll get the error

# l1=[1,3,4,5,6,6,7]
# # l3=l1+23#--> here we have one argument of int type and second one is of list type so we will get the error
#     # TypeError: can only concatenate list (not "int") to list
#     # + operator concatinat two list and returns the concatenated list
# l2=[23,2,3]
# l3=l1+l2
# l3=l1+[2]
# print(l3)
# plus v/s extend()
# --> + operator returns concatednated list(creates new object),but extend() method doesn't create new object
# --> both arg should be of list type for + operator, but in extend mehtod we can pass any iterable data type.

# a=[1,3]
# a.extend('abc')
# print(a)#[1,3,'a','b','c']


# * OPERATOR
# b=a*3
# print(b)#[1,3,'a','b','c',1, 3,'a','b','c',1,3,'a','b','c']

# COMPARISON OPERATOR : <,<=,>,>=,==,!=
    # in list COMPARISON we compare the first element of each list and on the basis of that we returns our resul
    # if i have 2 list :
    # l=[12,2,3,5]
    # l2=[12,2,3,5]
    # print(l<l2)#f
    # print(l<=l2)#t
    # print(l==l2)#t
    # print(l>=l2)#t

# MEMBERSHIP OPERATOR :in not in 
    # l=[12,2,3,5]
    # print(12 in l)#t
    # print(12 not in l)#f


# NESTED LIST:
# PRINT 3*3 MATRIX
    # BY 2 MEHTOD:

l=[[1,2,3],[4,5,6],[7,8,9]]

# mehtod1:
# for x in l:
#     print(x)

# method 2:
    # for i in range(len(l)):
    #     for j in range(len(l[i])):
    #         print(l[i][j],end=' ')
    #     print()


#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
# LIST COMPERHENSION
# l=[expression for x in sequece]
# l=[expression for x in sequece if condition]
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE
#NOTE NOTE NOTE#NOTE NOTE NOTE#NOTE NOTE NOTE

# l=[2*x for x in range(10)]
# print(l)
# l=[2**x for x in range(10)]
# print(l)
l=[x**2 for x in range(10) if x%2==0]
print(l)

















# a=257
# b=257
# print(id(a))
# print(id(b))
# c=2533
# d=c
# print(id(c))
# print(id(d))

# print('changing')
# a=454
# c=22
# print(a)
# print(b)
# print(c)
# print(c) 