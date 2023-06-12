
# concatenation
def test1():
    l=[]
    for i in range(1000):
        l=l+[i]
# append
def test2():
    l=[]
    for i in range(1000):
        l.append(i)
# comprehension
def test3():
    l=[i for i in range(1000)]
# list range
def test4():
    l=list(range(1000))

from timeit import Timer
print(Timer('test1','from __main__ import test1').timeit(number=1000))
print(Timer('test2','from __main__ import test2').timeit(number=1000))
print(Timer('test3','from __main__ import test3').timeit(number=1000))
print(Timer('test4','from __main__ import test4').timeit(number=1000))