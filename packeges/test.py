from pack1.module1 import f1
from pack1.sub_pack.module2 import f2
from Modules.math1 import sum1
exec('f1()')
exec('f2()')

print()
print('this is the package from diffrent location')
x=sum1(3,2)
