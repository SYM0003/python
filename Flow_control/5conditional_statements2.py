a,b,c=[eval(x) for x in input("Please enter two numbers:").split()]
if a>b and a>c:
    print(a)
elif b>c and a!=b!=c:
    print(b)
elif a!=b!=c:
    print(c)
else:
    print("all are equal")
