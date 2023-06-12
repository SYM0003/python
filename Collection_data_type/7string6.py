# write a program to find out the number of 
# white space present in the given string

s=input("Please enter a string\n")
s1=s.replace(" ","")
print(len(s)-len(s1))
print(s.count(" "))