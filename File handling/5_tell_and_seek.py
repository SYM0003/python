# tell() and seek() method

# tell method returns the index of the file pointer, more precisely it retuns 
# the index of the character on which it is pointing


# seek(ind) method moves corser(file pointer) to the given index in 
with open('abc.txt','w') as f:
    f.seek(4)#move cursor to 4th index
    print(f.tell())

