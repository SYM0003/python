# wap for generating the fake employee data for database testing and store it in 2d matrix
# data should contain following details:
# 1 employee name first letter capital name length should be greater than 5 and smaller than 8
# 2 employee no is a string of len=5 it starts with EN and follows three integer
# 3 employee salary should be between 30000 INR to 50000 INR 
# 4 location should be Indore,Pune,Banglore,Hydrabad and Chennai.

import random
alph_c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_s='abcdefghijklmnopqrstuvwxyz'
location=['Indore','Pune','Banglore','Hydrabad','Chennai']
l=[['e_name','e_no','e_sal','e_loc']]
data=dict()

e_name=[]
e_no=''
e_sal=[]
e_loc=[]
for i in range(10):
    e_name=random.choice(alph_c)+random.choice(alph_s)+random.choice(alph_s)+random.choice(alph_s)+random.choice(alph_s)
    e_no='EN'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    e_sal=random.uniform(30000,50000)
    e_loc=random.choice(location)
    sub=[e_name,e_sal,e_loc]
    if e_no in data:
        e_no='EN'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    data[e_no]=sub
# print(data)
for x in data:
    print(x,data[x])
