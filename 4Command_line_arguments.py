from sys import argv;
#This program is written for showing how does command line argument works in python
print("Printing all element except the first one:",argv[1:])
# console will give this argument because I
# gave this arguments from the command line.['4', '3', '2', '1', '3']
print("Printing all the elements :",argv)#will all element of argv
print("Printing the length of argv: ",len(argv))#will print the number of elements present in the argv.
# print all element one by one:
print("Printing all elements one by one ")
for x in argv[1:]:
    x=eval(x)#->some experimets by shyam
    print(x," Type: ",type(x))

# print the sum of the elements of argv;
sum=0
for x in argv[1:]:
    sum=sum+int(x)#orsum+=int(x)
print("The sum of command line argumets is:",sum)


# if pass this arguments through commnad line:
# path> py file_name.py 3 2 shyam verma
# compiler will seprate each command from space(" ") then 
# shyam  will be one  argument and verma will be second argument.
#  if we want to consider it as single argument then we will have to use : double cote(" ")
# path> py file_name.py 3 2 "shyam verma"<-like this


