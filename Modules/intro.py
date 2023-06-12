# module: we can consider it as a python file containing 
# similar function classes and  variables


# each python file is a module in itself
# from math1 import *

# print(sum1(5, 6))


# what is pyc file:

# basically when we import any python file as module than our
# pvm jenerate the machine level code for that file and it is saved under the file with extension pyc

# i.as in above block code we have imported the math1 file as module so the pyc file would must be generated 
# this file is generated so that if we need that file again some where than the pvm will use that pvm file instead of
# its orignal file






# # various syntax for improting module
# NOTE NOTE NOTE NOTE NOTE NOTE 
# import module_name
# import module_name1,module_name2
# import module_name1 as m1,module_name2 as m2
# from module_name import member
# from module_name import member
# from module_name import *
# from module_name import member1,member2
# from module_name import member as m1
# from module_name import member1 as m1,member2 as m2









# 
# # conflicts in importing modules

# # suppose we have imperted two mudles as below


# from module_name1 import *
# from module_name2 import *
# # and both have a function add(x,y)
# # if i call the function which add function would called by pvm
# # add(x,y)-> function of module_name2
# # concept behind it is simple that the pvm always call the latest
# # copy of it


# from math1 import *
# from math2 import *
# sum1(3,5)#the function of math2

# if you want to use the specific function of specific module and not able to use it due to this conflict
# than use should go for this two alternatives



# # import module in this manner
# # method1
# import math1
# import math2

# # method2

# from math1 import sum1 as s1
# from math2 import sum1 as s2




# how to find out the member of a moudle
# by using dir() and help()


help("Modules")