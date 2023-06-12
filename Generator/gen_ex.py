#generator for generating first n natural numbers
def gen_n(n):
    for i in range(n):
        yield i+1

# generator for generating fibonachi series

def fib(n):
    a,b=0,1
    i=1
    while i<=n:
        yield a
        a,b=b,a+b
        i+=1


x=fib(5)

for a in x:
    print(a)


