with open('e:\\shyam\\programing\\PYTHON\\File handling\\abc.txt','r') as f:
    data=f.read()#->will read all data from the file and return it as str obj
    print(data)
    f.seek(0)
    data=f.read(4)#->will read five character from the file, will start reading from the pointers current possition only
    print(data)
    f.seek(0)
    data=f.readline()#read one line from the file
    print(data)
    f.seek(0)
    data=f.readlines()#read all lines from the file and returns the list obj of the lines
    print(data)
    print('is file closed : {}'.format(f.closed))#False
print('is file closed : {}'.format(f.closed))#True






