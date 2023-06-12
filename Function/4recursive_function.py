def fac(n:int)->int:
    if n==0:
        return 1
    return n*fac(n-1);

print(fac(5))
print(fac(5))

def fib(n:int)->int:
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(5):
    print(fib(i),end=" ")