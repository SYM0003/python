#read number of list from the keyboard and print each element using loops
n=[eval(x)for x in (input("Please enter a list: ").split())]
# n=eval("input(Please enter a list:"))
# remove split and then see the diffrence b/w output
for x in n:
    print(x,end=" ")

print("\n",n)