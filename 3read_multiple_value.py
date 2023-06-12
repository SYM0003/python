x,y=[int(a) for a in input("Please enter 2 values:").split()]
print(x+y)

#read 2 values only by one line which should be comma(,) seprated.
x,y=[float(a) for a in input("Please enter 2 values:").split(",")]
print(x+y)


#read multiple value only by one line which may be deffrent type and must be seprated by comma(,)
a,b,c=[eval(n) for n in input("Please enter three values:").split(",")]
print("The type of a,b,c is :")
print(type(a))
print(type(b))
print(type(c))
print("The sum of a,b,c is :",a+b+c);