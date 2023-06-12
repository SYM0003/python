#About: This program is written to print that the particular character 
# is present in the given string or not and print the occurences of the string.


s=input("Enter the main string\n")
# s="sahyaamavermaa"
subs=input("Enter the substring\n")
count=0
pos=0
lens=len(s)
lensubs=len(subs)
while True:
    i=s.find(subs,pos,lens)
    if (i!=-1):
        print("found at index {}".format(i))
        pos=i+lensubs
        count+=1
    else:
        break
cnt=subs,s.count(subs)
#string.count(substring)>>is a build in function for findint the number of occurences 
# of the substring in given string
print("substring %s was present in the string for %d times" %(cnt))
print("substring %s was present in the string for %d times" %(subs,count))
