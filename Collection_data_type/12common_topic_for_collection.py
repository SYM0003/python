# # MERGING OF COLLECTION
# #list-->by using + operator
# #tuple-->by using + operator
# #set-->by using update method
# #dict-->by using update method

# #list
# l1=[10,20,30,40]
# l2=[50,60,70]
# l1+=l2
# print(l1)

# #set
# s1={10,20,30,40}
# s2={50,60,70}
# s1.update(s2)
# print(s1)


# #dict
d1={'B': 0, 'C': 0, 'D': 0, 'F': 0, 'G': 0, 'H': 0, 'J': 0, 'K': 
0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'T': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
d2={'A':0,'E':0,'I':0,'O':0,'U':0}
# d1.update((['a',5],['b',3],('c',2)))
# print(d1)




# #OPTIONAL METHOD -->USING *x-->read as all element present inside x NOTE NOTE
#                           # **x--> all key value present in the x (applied for dict)
# d3={**d1,**d2}
# print(d3)

# # use 1: merging hatrogenious collection in a single collection
# l=[1,3,4,5,45,6,56,45,44]
# t=('a')
# s={40,60,70,80}

# common=[*l,*d,*s]
# print(common)



l=[[1,3,4,5,45,6,56,45,44],('a'),{40,60,70,80}]
l2=[*l[0],*l[1],*l[2]]
print(l2)





