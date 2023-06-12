# # f=open('abc.txt','w')
# f=open('e:\\shyam\\programing\\PYTHON\\File handling\\abc.txt','w')
# f.write('this is the first line\n')
# l=['a','b','c']
# f.writelines(l)
# f.write('\nthis is new line')
# f.close()


# 
# r+ and a+ # overriding will not be done in this two mode
# w+ overriding will be done

# # case 1
# f=open('abc2.txt','r+')
# f.readline()
# print(f.tell())
# f.write('this is new\n')
# f.seek(14)
# f.write('this is new\n')#->it will starti writing from the 14 index

# case 2
f=open('abc2.txt','a+')
f.readline()
print(f.tell())
f.write('this is new\n')
f.seek(14)
f.write('this is new\n')#->it will starti writing from the end of the file only without carring of the cursor

# case 2
f=open('abc2.txt','w+')# new empty file will be created,replacing old file if exist
f.readline()
print(f.tell())
f.write('this is new\n')
f.seek(14)
f.write('this is new\n')#->it will starti writing from the end of the file only without carring of the cursor
