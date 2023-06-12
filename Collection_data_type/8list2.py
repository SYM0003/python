# # CREATE A LIST WITH SQUARES OF FIRST 10 NATURAL NUMBERS
# l=[]
# for x in range(1,11):
#     l.append(x**2)
# print(l)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# # method 2: list COMPERHENSION
# l = [x**2 for x in range(1,11)]
# print(l)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # CREATE A LIST WITH SQUARES OF FIRST 20 EVEN NATURAL NUMBERS
# # method 1:
# l=[]
# for x in range(1,21):
#     if x%2==0:
#         l.append(x**2)

# # method 1:
# l=[x**2 for x in range(1,21) if x%2==0]
# print(l)
# print(len(l))


# # YOU HAVE GIVEN A LIST OF WORDS IN BELOW FORMAT:
# # l=['shyam','vishal','shubham']
# # return list l1 =['s','v','s']

# l=['shyam','vishal','shubham']
# l1=[]
# for x in l:
#     l1.append(x[0])
# print(l1)#['s', 'v', 's']

# l=['shyam','vishal','shubham']
# l1=[word[0] for word in l]
# print(l1)#['s', 'v', 's']








# # YOU HAVE GIVEN 2 LIST CONTAINING NUMBERS YOU HAVE TWO PRINTT THE LIST L3 WHICH HAS ELEMENT PRESENT IN L1 BUT NOT IN L2
# l1=[1,2,3,4,5,64,24]
# l2=[1,2,3,4,5,75,23]
# l3=[]
# for x in l1:
#     if x not in l2:
#         l3.append(x)
# print(l3)#[64, 24]

# # mehtod1:
# l1=[1,2,3,4,5,64,24]
# l2=[1,2,3,4,5,75,23]
# l3=[x for x in l1 if x not in l2]
# print(l3)#[64, 24]



# # YOU HAVE GIVEN 2 LIST CONTAINING NUMBERS YOU HAVE TWO PRINTT THE LIST L3 WHICH HAS ELEMENT PRESENT IN BOTH GIVEN LIST
# l1=[1,2,3,4,5,64,24]
# l2=[1,2,3,4,5,75,23]
# l3=[]
# for x in l1:
#     if x in l2:
#         l3.append(x)
# print(l3)#[1, 2, 3, 4, 5]

# # mehtod1:
# l1=[1,2,3,4,5,64,24]
# l2=[1,2,3,4,5,75,23]
# l3=[x for x in l1 if x in l2]
# print(l3)#[1, 2, 3, 4, 5]


# # WAP FOR FOLLOWING REQUIREMENT
# s='THE BROWN FOX JUMP OVER THE LAZY DOG'
# w=s.split()
# # w=['THE', 'BROWN', 'FOX', 'JUMP', 'OVER', 'THE', 'LAZY', 'DOG']
# # output=[['THE',3],['BROWN',5],['FOX',3],['JUMP',4],['OVER',4],['THE',3],['LAZY',4],['DOG',3]]
# output=[]
# for x in w:
#     output.append([x,len(x)])
# print((output))#[['THE', 3], ['BROWN', 5], ['FOX', 3], ['JUMP', 4], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE 
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE 
# output=[[x,len(x)] for x in w]
# print((output))#[['THE', 3], ['BROWN', 5], ['FOX', 3], ['JUMP', 4], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE 
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE 


# # WAP PROGRAM TO DISPLAY UNIQUE VOWELS PRESENT IN THE GIVEN WORD
# w='shyam'
# w=w.upper()
# v='AEIOU'
# l=[]
# for x in w:
#     if( x in v and x not in l):
#         l.append(x)
# print(l)


# l=[]
# l=[x for x in w if x in v  and x not in l]
# print(l)