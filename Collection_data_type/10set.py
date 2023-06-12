# if we wan't to store the data whose order is not important,
# we wan't only unique values than we should use set data type

# set: set is group of unique object werer order is not important
# set v/s list
# set: set is group of uninque object where order is not preserved, set is mutable 
# data structure, if we wan't to perform serach operation mostly than we should go 
# for set data structure



# s2={3,4,1,5,64}

# print(type(s1))
# print(s1 == s2)
# print(s2.difference(s1))


# # CREATION OF SET
    # s1={1,3,4,5,6}
    # d={10:'shyam',2:'shubham'}
    # s1=set(d)#? NOTE

    # s1=set('enter any set of element')
    # print(s1)#{'m', 'r', 'f', 'a', 't', 's', ' ', 'e', 'o', 'y', 'n', 'l'}
    # s1=set(input('enter any set of element').split())#{'shyam'}
    # print(s1)#{'shyam'}

# # HOW TO CREATE EMPTY SET?
    # s={}#--> we can't define empty set in this manner
    # print(type(s))#<class 'dict'>
    # s1=set()
    # print(type(s1))#<class 'set'>
# # HOW TO ADD ELEMENT IN EXISTING SET?--> TWO METHOD
# # there are two method() for this :
    # # add()--> takes hasable object and add it to the given set. i.e:
    # # list is not hashable and all fundamental data types,tuple are hashable,
        # s={1,3,5}
        # s.add(2)#--> will add two in s.
        # print((s))#{1, 2, 3, 5}
        # s.add([1,3])#since list is not hashable so can't add ,TypeError: unhashable type: 'list'
    # # update()--> takes itratable object and add each element of that object in the set
        # s={1,34,56,3}
        # l=[1,3,5,56]
        # s.update(l)
        # print(s)#{1, 34, 3, 5, 56}
        # s.update(1)#TypeError: 'int' object is not iterable

# # WHAT WILL BE THE VALUE FOR S1 AND S2
    # s1={'missisippy'}#{'missisippy'}
    # s2=set('missisippy')#{'y', 'p', 'm', 's', 'i'}

# every element should be hashable
# # WHICH ARE VALID
    # s2=set()
    # # s2.add([1,3,4])#not valid
    # s2.add((1,3,4))#valid
    # s2.update([1,3,4])#valid
    # s2.update((1,3,4))#valid
    # s2.add(range(0,10))#valid
    # s2.update(range(0,10))#vlaid
    # # NOTE NOTE NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE NOTE NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE NOTE
    # # s2.update([1,2,[3,4]])#not valid:why?
    # # NOTE NOTE NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE NOTE NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE NOTE
    # print(s2)
    # for x in s2:
    #     print(type(x))





# NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE
# IS SET ELEMENT IS STORED BY HASHING TELL WHAT IS HASING AND IMPORTACE OF 
# --> OUT OF SYLLABUS HASHIN SEARCH o(1)

# SEARCHING ELEMENT IN LIST O(N)
# SEARCHING ELEMENT IN SET O(1)
#  
# # HOW TO REMOVE ELEMENT FROM THE SET 4 methods
    # # remove(value): deletes the given value if present in the set else give KeyError
    # # discard(value):NOTE same as remove(), if value available remove it else ingore (doesn't give any error) NOTE
    # # pop()-->deletes a random element from the set (by appling hasing algo internal things))
    # S={1,3,4,5}
    # S.discard(3)
    # S.pop()
    # # S.remove(3)
    # S.discard(3)
    # print(S)






# NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE
# #  plus operator and star operator for set(imp) NOTE
# s1={1,3,4,554}
# s1={13,6,7,84,3}
# s3=s1+s2
# s3=s1+3
# # NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE


# SPECIAL MATHEMATICAL OPETATION FOR SET
# # s1={1,3,4,554}
# # s1={13,6,7,84,3}
# # s1|s2 --> elemnt present either in s1 or s2-->union()
# # s1&s2 --> elemnt present  in s1 and s2 both -->intersactin()
# # s1^s2 --> elemnt present either in s1 or s2 but not in both-->symmetric_diffrence()
# # s1-s2 --> elemnt present in s1 but not in s2--> diffrence()



s1={1,3,4,554}
s2={13,6,7,84,3}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)
print(s1.difference(s2))
print(s1-s2)
print(s1.symmetric_difference(s2))
print(s1^s2)



# MEMBERSHIP OPERATOR: in,not in
# COMPREHENSION

# # WAP TO DELETE DUPICATE PRESENT IN THE LIST
# # METHOD 1:
# n=eval(input('enter a list of values:\n'))

# l=[]
# for x in n:
#     if x not in l:
#         l.append(x)
# print(l)#[1, 34, 5, 67, 4, 2, 3]
# # METHOD 2:
# s=set(n)
# print(s)#{1, 34, 67, 4, 5, 2, 3}

# # WAP PROGRAM TO PRINT DIFFRENT VOWEL PRESENT IN THE GIVEN WORD
    # n=input('enter a WORD :\n').lower()
    # # METHOD 1:
    # v=['a','e','i','o','u']
    # r=[]

    # for x in v:
    #     if x in n:
    #         r.append(x)
    # print(r)

    # # METHOD 2:
    # r2=set(n)
    # v={'a','e','i','o','u'}
    # print(r2&v)


