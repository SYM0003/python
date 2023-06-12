
# # ********************************************************************************
# # 1.dict()--> may use for:
# # 2.len()--> no.of pair(items) in dict
# # 3.d.get(key)--> returns the corospoindig value assosiated with the key,
# # 4.d.pop(key)--> delete the key value pair and returns the value
# # 5.d.popitem(None)-->removes an arbitary item and 
# # 6.d.keys()-->returns keys present in d--> data type dict_keys
# # 7.d.values()-->returns values present in d--> data type dict_values
# # 8.d.items()-->returns dict_items type collection 
#                 #contening each pair of key value as a tuple
# # 9.setdefault(k,v)--> if k is already available in d than it will return corosponding value
#                       #  if k is not available in d than it will add key value pair of k,v in dict
# # 10.d.update(d2)--> will update the dict with key value of d2
# # 11.d.copy()-->create new object containg same key values of d
# # 12.d.fromkeys(iteratable)--> creates key value pairs for each value in iteratable and asing None value to each of them
# # ********************************************************************************



# if we want to store a group of pair(key value) as single entity than we should go for dict data type
# in dict we can store the group of key value pair as single entity where order is not preserved and hatrogenious data is allowed
# dict is growable in nature
# we can access the value of dict by the help of its key.
# in dict duplicate keys are not allowed but duplicate values are allowed


# WAP PROGRAM TO ENTER NAME AND COROSPOINDING MARKS FROM THE USER:

# s={}
# i=0
# n=int(input('enter no of student:\n'))
# while i<n:
#     name,marks=input('enter your name and your marks in math').split()
#     s[name]=marks
#     i+=1

# for x in s:
#     print("marks for {:<10}: {:^5}".format(x,s[x]))

# s={}
# while True:
#     name,marks=input('enter your name and your marks in math').split()
#     s[name]=marks
#     option=input('do you want to stor more data? enter yes or no:\n')
#     if option.lower()=='no':
#         break

# for x in s:
#     print("marks for {:<10}: {:^5}".format(x,s[x]))

# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # REMOVE THE BUG FORM THIS PROGRAM
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE







# # HOW TO UPDATE DICT OR ADDING NEW VALUE?
# d={1:3,3:5,2:5,6:3}
# # method1:
# print(d)
# d[15]=46#-->will add new key because there is no key for given data
# print(d)
# d[15]=2#-->will update the value of key:15 
# print(d)

# # HOW TO DELETE A KEY VALUE PAIR FROM VALUE?
# d={1:3,3:5,2:5,6:3}
# # method1:
# del(d[1])
# # mehthod2: 
# # NOTE NOTE NOTE NOTE NOTE NOTE
# # syntax:-->dict.__delitem__(key)
# d.__delitem__(1)
# # NOTE NOTE NOTE NOTE NOTE NOTE

# # HOW TO DELETE ALL ELEMENT FROM THE KEY?
# d={1:3,3:5,2:5,6:3}
# # METHOD 1:
# del(d)
# # METHOD 2:
# d.clear()

# # del(d) vs d.clear()
# # del will delete the reffrence variable also and we won't
# # be able to access that element it will be ready for garbage collection

# # on the other hand clear() will just del the element present in the give dict


# # IMPORTANT FUNCTION AND METHODS RELATED TO DICTIONARY:
# # 1.dict()--> may use for:
#                     # creatig empty dict
#                         # d=dict()

                    
#                     # d=dict({('a',100),('b',35),('c',4)})
#                     # d=dict((('a',100),('b',35),('c',4)))
#                     # d=dict([('a',100),('b',35),('c',4)])
#                     # print(d)
# # 2.len()--> no.of pair(items) in dict
# # 3.d.get(key)--> returns the corospoindig value assosiated with the key,
#     # if key is not there what will happen?
#     # NOTE NOTE NOTE NOTE NOTE NOTE NOTE
#     # diffrence in d[key] and d.get(key)
#         # both work same but the diffrent is identified when key is not in the dictionary
#         # when key not in dict:
#         # d[key]-->gives keyerror
#         # d.get(get)-->returns NONE, if we wan't any other value isntead of none we can sate default_value=value
#     # NOTE NOTE NOTE NOTE NOTE NOTE NOTE
#     # d.get(2,default_value=any default value)

# # 4.d.pop(key)--> delete the key value pair and returns the value
    # d={1:3,2:5,3:4}
    # popped=d.pop(1)
        # # delete the key value pair and returns value
        # # if key not in dict we get KeyError

    # print(popped)#-->will print 3 because 3 is the value assosiated with 1
    # # we can also use del(d[key])--> it doesn't return any thing
    # # popped=del(d[2])#-->invalid syntax
    # del(d[2])#--> delete the key value pair(2:5)
# # 5.d.popitem(None)-->removes an arbitary item and 
# #                   returns the tuple of key value pair
# #                    if there is no item than it will give KeyError

    # d={1:3,2:5,3:4,4:2}
    # print(d.popitem())#(4, 2)
    # print(d.popitem())#(3, 4)
    # print(d.popitem())#(2, 5)
    # print(d.popitem())#(1, 3)




# d={1:3,2:5,3:4,4:2}
# # 6.d.keys()-->returns keys present in d--> data type dict_keys
# d={1:3,2:5,3:4,4:2}
# print(d.keys())#dict_keys([1, 2, 3, 4])
# print(type(d.keys()))#<class 'dict_keys'>

# # 7.d.values()-->returns values present in d--> data type dict_values
# d={1:3,2:5,3:4,4:2}
# print(d.values())#dict_values([3, 5, 4, 2])
# print(type(d.values()))#<class 'dict_values'>

# # 8.d.items()-->returns dict_items type collection contening each pair of key value as a tuple
# d={1:3,2:5,3:4,4:2}
# print(d.items())#dict_items([(1, 3), (2, 5), (3, 4), (4, 2)])
# print(type(d.items()))#<class 'dict_items'>




# # ********************************************************************************

# d={1:3,2:5,3:4,4:2}
# items=d.items()
# for k,v in items:
#     print('key is ',k,end=' ')
#     print('value is',v)
#     # key is  1 value is 3
#     # key is  2 value is 5
#     # key is  3 value is 4
#     # key is  4 value is 2
# # ********************************************************************************




# # 9.setdefault(k,v)--> if k is already available in d than it will return corosponding value
                        #  if k is not available in d than it will add key value pair of k,v in dict
    # d={1:3,2:5,3:4,4:2}
    # d.setdefault(1,6)#since 1 is already in the d so it will return the value already associated with it 
    # print(d.setdefault(1,6))#3
    # d.setdefault(13,5)#sice 13 is not a key of d so this key value pair will be added to d
    # d.setdefault(13,5)#sice 13 is not a key of d so this key value pair will be added to d
    #                   #and won't return any thing 
    # print(d)
    # NOTE NOTE setdefault()vs d[key]=value NOTE NOTE

# # 10.d.update(d2)--> will update the dict with key value of d2
    # d1={1:'shyam',2:'rohan',3:'vishal',4:'shubham'}
    # d2={5:'rishi',6:'mahesh',7:'vishesh'}
    # d1.update(d2)
    # print(d1)#{1: 'shyam', 2: 'rohan', 3: 'vishal', 4: 'shubham', 5: 'rishi', 6: 'mahesh', 7: 'vishesh'}


# # 11.d.copy()-->create new object containg same key values of d
# d={1:3,2:5,3:4,4:2}
# d1=d.copy()
# print(id(d is d1))#False


# # 12.d.fromkeys(iteratable)--> creates key value pairs for each value in iteratable and asing None value to each of them
    # d={}.fromkeys(range(9))
    # print(d)
    # # {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}




# # ********************************************************************************
# # WAP PROGRAM TAKE DICT FROM THE USER AND PRINT THE SUM OF THE VALUES
    # d=eval(input('enter a dict'))#{'a':12,'b':23,'c':234}
    # # METHOD 1:
    # s=sum(d.values())#269
    # print(s)#269
    # s1=0

    # # METHOD 2:
    # for x in d.values():
    #     s1+=x
    # print(s1)



# # WAP PROGRAM TO FIND NO.OF OCCURRENCES OF EACH LETTER IN THE GIVEN STRING
# s='shyammmmmambmmcdmmefmfaaaaafdfhdkjsj'
# # METHOD 1(here is two methods comined):
# s1=[]
# s2=''

# for x in s:
#     if x not in s2 and x not in s1:
#         n=s.count(x)
#         print('{} present in the string for {} times'.format(x,n))
#         s1.append(x)
#         s2+=x

# # METHOD 2:
# d={}
# for x in s:
#     if x not in d:
#         n=s.count(x)
#         d[x]=n
#         print('{} present in the string for {} times'.format(x,n))

        
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE 
# # SOLVE THIS PROBLEM WITHOUT USING count() method
# # SOLVE THIS PROBLEM  USING dict.itmes() method
# # METHOD 3:
# s='shyammmmmambmmcdmmefmfaaaaafdfhdkjsj'
# d={}
# for x in s:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]+=1
# for k,v in d.items():
#     print("{} occures {} times".format(k,v))


# # SOLVE THIS PROBLEM  USING dict.get() method
# s='shyammmmmambmmcdmmefmfaaaaafdfhdkjsj'
# d={}

# for x in s:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print("{} occures {} times".format(k,v))




# # WAP PROGRAM TO FIND NO.OF OCCURRENCES OF EACH vowel IN THE GIVEN STRING
# s='shyammmmmambmmcdmmeEfmfaaaaafdfhdkjsj'
# d={'a':0,'e':0,'i':0,'o':0,'u':0}

# for x in s:
#     if x.lower() in d:
#         d[x.lower()]+=1
# for k,v in d.items():
#     print('{} occures {} times'.format(k,v))




# WAP TO ACCEPT STUDNET NAME AND MARKS FROM THE KEYBOARD AND WITH THAT 
# DATA CREATE A DICTIONARY. ALSO DISPLAY STUDENT MARKS BY TAKING NAME AS INPUT.

n=int(input('enter the number of student\n'))
d={}
while len(d)!=n:
    name=input('enter student name\n')
    marks=eval(input('enter the list of marks for {}\n'.format(name)))
    d[name]=marks

while True:
    name=input('enter student name for getting the marks detail\n')
    if name in d:
        print('Marks for {} are :{}'.format(name,d[name]))
    else:
        print('student not found')

    option=input("do you want to see another student's marks? enter yes|no\n").lower()
    # while True:
   
    while True:
        if option in ['yes','no']:
            break
        option=input('invalid option please enter yes|no\n').lower()
    if option =='no':
        break
        
print('Thankyou for using our services have a good day')
# NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE  NOTE
# DICT COMPREHENSION # DICT COMPREHENSION # DICT COMPREHENSION
# NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE  NOTE NOTE NOTE NOTE NOTE  NOTE


# # syntax: dict={key:value for key in iteratable condition}

# # creating dict of alphabate(consonate only)
# d={chr(x+65):0 for x in range(26) if chr(x+65) not in ['A','E','I','O','U']}
# print(d)
# print(type(d))























