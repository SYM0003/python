# tuple is immutable version of list data type
# once we create the tuple object than we can't delete(can't perform manupulation operations) on it
# t=(2,3,4)
# # we can also define tuple as below
# t=2,3,4
# print(type(t))

# t[0]=2#TypeError: 'tuple' object does not support item assignment
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # if you are putting only one value in tuple you must put comma(, after that value)
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # WHICH ARE TUPLE AND WHICH ARE NOT
# t=()
# t=(10)
# t=(10,)
# t=10
# t=10,
# t=(1,2,3)
# t=1,2,3
# t=1,2,3,



# # tuple is mote efficent as compare to list
# # tuple occuies less memory than list
# l=[1,2,3,4,5,6]
# t=(1,2,3,4,5,6)
# from sys import getsizeof
# print(getsizeof(l))#152
# print(getsizeof(t))#88






# IN REAL LIFE WHERE WE USE LIST AND TUPLE




# CREATION OF TUPLE
# t=(10)#-->it is not tuple it is a integer
# t=(10,)#-->tuple
# t=()#-->empty tuple
# t=10#-->int
# t=10,-->tuple
# t=(1,2,3)
# t=1,2,3
# t=1,2,3,

# t=eval(input('enter a tuple'))


# # ACCESSING TUPLE ELEMENT
# t=(1,3,5,6,7,2)
# # by using slice 
# print(t[1:2])
# # by using index
# print(t[1])



# # mathematcialmathematcial operator
# # + operator
# # this work as concatenation operator for two or mor tuple
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# t2=(1,2,34,5,4,5)
# t3=(13,4.234,34,64)
# t3=t2+t3
# t4=t2+t3
# print(t3)
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # * operator 
# t2=(1,2,34,5,4,5)
# t3=(13,4.234,34,64)
# t4=t3*3
# print(t4)
# # function and method related to tuple
# t=(1,2,3,5,5,3,6,4,34212,23)
# # find the length of the tuple
# print(len(t))
# # find the total occurence of given element in the tuple
# print(t.count(3))
# # index of given value
# print(t.index(3))
# # sorting tuplet
# t3=sorted(t)







# # tuple packing and unpacking

# a,b,c,d=1,2,3,4,
# t=[a,b,c,d]#-->packing
# a,b,c,d=t#-->unpacking
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE: numbers of reffrenc variable should be equal to len(t) for unpacking if 
# # it won't than it will give error

# a,b,*c=t
# # this line means assign the first element of t to and second element of t to b and 
# # asign the tuple of remaing items to c
# # here t =(1,2,3,4,)
# # than a =1,b=2 ,c =(3,4,)-->type(c)=<class 'tuple'>



# # tuple comprehension -->not available--> generator
# t=(x*x for x in range(6))
# print(type(t))#<class 'generator'>
# # tuple vs list-->def,comprehension,performance,hasabilit
# # imutabl                mutabl
# # ordered sequence of values
# # can access by slicing and indexing
# # can't manupulate data   can manupulate data
# # hasing applicable       hasing not applicable
# #





# # WAP TO TAKE TUPLE OF NUMBERS FROM KEYBOARD AND PRINT IT'S SUM AND AVG.
# # MEHTOD 1:
# t=eval(input('Please enter a tuple'))
# print(type(t))
# print(t)
# sum1=0
# for x in t:
#     sum1=sum1+x
# print('the sum1 of given tuple elements is {}'.format(sum1)) 
# print('the average of given tuple elements is {}'.format(sum1/len(t))) 

# # MEHTOD 1:
# s=sum(t)
# a=sum(t)/len(t)

# print(a)
# print(s)