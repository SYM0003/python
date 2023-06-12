#take two numbers from the user and return the maximum of them using conditional statements;

a,b=[int(x) for x in input("Please enter two numbers:").split()]
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("Both are equal")
