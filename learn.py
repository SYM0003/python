# s="shyam"
# print(s*0)#will print empty string


# a,b=2,3
# # relational operartors 
# print(a<b)#t
# print(a>b)#f
# print(a<=b)#t
# print(a>=b)#f
# print(a==b)#f

# NOTE: THE ABOVE THE CONCEPT ALSO APPLY ON STRING ALSO

# print('a'<5)-->will give type error you can't compare two diffrent
# data type values
# print(ord("a")) #97
# print(ord("2")) #50
# a=3
# b=30
# if(a>b):
#     print("a is greater than b")
# else:
#     print("a is smaller than b")



# print(ord('297'))-->you can't pass multiple character 
#  to ord()function it accept only single character


# print(10<30<34<2)#--> will give false, it will not give error

# euality operator will not give error ever  if we are comparing 
# the two diffrent data types

# print("shyam"==3)
# print("shyam"!=3)
# print("shyam"!="rohan")
# print("shyam"==shyam)-->NameError: name 'shyam' is not defined




# NOTE
# logical operator: and or not:
# and: if both operands are true than only it will return true else return false
# or:  if altleast one operand is true than it will return true else return false
# not: return comlement of the operands and it is unary operator

# print(10 and 0)#0
# print(0 and "e")#0
# print(10 and "e")#"e"
# print("shyam" and 4)#4
# print(10 or 0)#10
# print(10 or "sk")#10
# print(0 or "shyam")#'shyam'
# print("" or "")#''
# print(not 1)#False
# print(not 0)#True
# print(not "1")#False
# print(not [])#True

#  is vs ==
# l1=[1,3,2,5]
# l2=[1,3,2,5]
# l3=l2

# print(l1 is l2)#False
# print(l1 is l3)#True
# print(l1 == l2)#True
# print(l1 == l3)#True

# NOTE
# bitwise operators:
# & | ^ ~ << >>
# these operators are applicable only for int and bool type



# a=4;
# b=5;
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)#-5

# ------------------#
    # a=4=000000000......100
    # 1's complement of 4:
    #     111111111......011
    # most significant bit is 1 so it will represent a negative no
    # and remaing bits will be represted as 2's comlement 
    # 2's comlement of remaing 31 bits:
    #     get 1's com of those bits:
    #     0000000000........100
    #     and 1 bit in it:
    #     000000000000......101=5
    #     100000000000......101=-5

# ------------------#





# shift operators:
# << left shift o

    # 10<<2
    # 0000000001010-->10
    # 2 bit left shift 0f 10
    # 0000000101000-->40
    # y=40
    # print(bin(y))#0b101000

    #100000001010-->>10
    #100000
# >> right shift o
    #print(10>>2)#2
    # 0000000001010-->10
    # vacant cells will be filled by sign bit
    # 0000000000010--2
    # print(10>>2)



    # print(-10<<3)
    # 00000000001010-->10
    # 1's:
    # 11111111110101
    # add 1 for 2's:
    # 111111...11110110-->-10
    # -10>>3:
    # NOTE:sign bit won't be shifted or will be changed"
    # 111111111...11110-->
    # now will have to find the 2's of this one also
    # 1's:
    # 100000000...00001-->
    # 2's:add 1
    # 100000000...00010-->-2
    # print(-10>>3)

    # asignment operator:used to asign values to the variables
    # x=4
    # 

    # some time this operators get combined with other operator and 
    # know as compound asignment operator. :
    # +=,-=,*=,/=/,%=,//2,**==,&=,|=,^=,<<=,>>=

    # a=4
    # b=4
    # b=3
    # c=4
    # d=4
    # e=4
    # f=4
    # d/=3


    # a+=3#a=7
    # b-=3#b=1
    # c*=3#c=4*3
    # d**=3#d=d**3
    # e//=3#e=e//3
    # f%=3#f=f%3
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)

    #there is no concept of increment and decrement operator concept:x--,x++,++x,--x
    # NOTE:
    #       X--  : will give syntax error
    #       X++  : will give syntax error

    #       ++X  : won't give syntax error 
    #       --X  : won't give syntax error
                    # : -(-X)

    # ternary operator:
    # if there are more than three operands in the statemet than it is gonna consider as 
    # ternary operator:
    # syntax:
    # x=a if a<b else b

    # a=int(input("Please enter a value"))
    # b=int(input("Please enter a value"))

    # x=a if a<b else b
    # print(x)
            
    # a,b,c=15,2,40
    # min=a if a<b and a<c else b if b<c else c
    # max=a if a>b and a>c else b if b>c else c
    # print(min)#2
    # print(max)#40
    # a=234
    # b=23
    # print("a is smaller than b" if a<b 
    #       else "a is greater than b" if a>b 
    #       else "both are eaul")



# SPECIAL OPERATOR:
    # identity operators : is, is not
    # a=10
    # b=10
    # print(id(a))#----------
    # print(id(b))#----------
    # print(a is b)#True
    # print(a is not b)#False

    # a="shyam"
    # b="shyam"
    # print(id(a))
    # print(id(b))
    # print(a is b)#True
    # print(a is not b)#False

    # a=[1,3,4]
    # b=[1,3,4]
    # print(id(a))
    # print(id(b))
    # print(a is b)#False
    # print(a is not b)#True



# MEMBERSHIP OPERATOR:
    #NOTE: obj in collection--> returns true if collection else returns false
    #NOTE: obj not in collection--> returns false if collection else returns true
    
    # we can check the membership operator for checking that the 
    # perticular value is part of the collection(string,list....etc) or not

    # s="durga sir is the greatest teacher of PYTHON"
    # print("d" in s)#True
    # print("d" not in s)#False

    # s=["shyam","Rohan","vishal"]
    # print("s" in s[0])#True




# MODULES:-someting like library (same like header filse of c/cpp)
    # it is python source file which may contain some classes, variables, methods and 
    # functions.
    # NOTE: modules also known as libraries.

    # import math
    # print(math.pi)

#PACKAGE: A folder of groups of MODULES.
#LIBRARY: LIBRARY IS A GROUP OF SIMILAR PACKAGES.

#ALIASING
    # import math as m
    # print(m.pi)#3.14159...
    # print(m.pow(2,3))#2**3

#ACCESSING THE MODULE MEMBER DIRECTLY
    # from math import *
    # print(pi)
    # print(pow(2,3))


#alias name for the member of the module
    # from math import pi as p
    # print(p)
    # import math
    # print(dir(math))#will give the list of members of math module
    # print(math.isqrt(12))#will give the square root value of neares full squar value (here ans root(9)=3)
    # print(math.ceil(2.3))#3
    # print(math.floor(2.3))#2

    # there is random value which used to use generato random value
    # import random
    # print(random.randint(1,5))
    # print(dir(random))


#INPUT AND OUTPUT STATEMENTS:

    # there were 2 type of input statements in python 2:
    # raw_input()-->always returns string type
    # input()--> returns the result type what ever we provided


    # but in python 3 there is only 1 input statement:
    # input()-->works like raw_input()

    # x=bool(input("Please enter a value:"))
    # print(type(x))
    # print(x)

    #NOTE print(int(input("Please enter x\n"))+int(input("Please enter y\n")))
    #NOTE print("The sum is",int(input("Please enter x\n"))+int(input("Please enter y\n")))
    

    # eno=int(input("Please enter employee number:"))
    # ename=input("Please enter employee name:")
    # esal=int(input("Please enter employee salary:"))
    # eaddr=input("Please enter employee address:")
    # # married=bool((input("Is employee maried or not:[True(1) or False(0)]")))
    # # married=bool(int(input("Is employee maried or not:[True(1) or False(0)]")))
    # married=eval(input("Is employee maried or not:[True(1) or False(0)]"))

    # print("Please confirm details:")
    # print("Number:",eno)
    # print("Name:",ename)
    # print("salary:",esal)
    # print("address:",eaddr)
    # print("married status:",married)


# EVAL FUNCTION:TAKES STRING ONLY AND EVALUATE THE 
# ENTERNAL VALUE(TYPE ) OF STRING.


# print(eval("3+4+3"))

# x=eval(input("enter some data\n"))
# print(x)
# print(type(x))
    # -----------------
    # [4,7,4,9]
    # [4, 7, 4, 9]
    # <class 'list'>


    # (1,3,"SHYAM")
    # (1, 3, 'SHYAM')
    # <class 'tuple'>

    # {2:"SHYAM",3:"KHUSHI"}
    # {2: 'SHYAM', 3: 'KHUSHI'}
    # <class 'dict'>

    # -----------------
    # x=eval(input("Please enter some value\n"))
    # print(x)
    # print(type(x))
    # -----------------
        # e:\shyam\programing\PYTHON>py learn.py
        # Please enter some value
        # "shyam"-->>NOTE entered value
        # shyam
        # <class 'str'>

        # e:\shyam\programing\PYTHON>py learn.py
        # Please enter some value
        # shyam -->>-->>NOTE entered value
        # Traceback (most recent call last):
        #   File "e:\shyam\programing\PYTHON\learn.py", line 354, in <module>
        #     x=eval(input("Please enter some value\n"))
        #   File "<string>", line 1, in <module>
        # NameError: name 'shyam' is not defined


    # -----------------


        # x=eval(input("enter a tuple:\n"))
        # print(type(x))
        # print(x)

        # 1,2,3,4,5,6,6
        # <class 'tuple'>
        # (1, 2, 3, 4, 5, 6, 6)

        # x=3 if (3 != True) else 4
        # print(x)


        # import random, math

        # print(random.randint(1, 700))
    # n=int(input("Please enter a number\n"))
    # a=1
    # while (n!=0):
    #     a=a*n
    #     n=n-1

    # print(a)

    # l="1 3 3 4"
    # s=l.split()
    # print(type(s))
    # print(s)

# SPLIT()
    # l="1 3 3 'shyam'"
    # s=[eval(x) for x in l.split()]
    # # split function always returns list data type.
    # print(s)
    # print(type(s))


    # # UNPACKING CONCEPT
    # a,b,c,d=l.split()
    # print(a)#1
    # print(b)#3
    # print(c)#3
    # print(d)#'shyam'



#HOW TO TAKE MULTIPLE VALUES IN SINGLE LINE
    #LIST COMPPREHENSION
    # s,t,u,v=[eval(x) for x in input("Please enter values").split()]
    # # r=[eval(x) for x in s.split()]
    # print(type(s))
    # print(type(t))
    # print(type(u))
    # print(type(v))

#   READ TWO INT VALUES FROM KEYBOARD AND MULTIPY THEM

    # a,b=[int(x) for x in input("Please enter two int values:\n").split("")]
    # # a,b=[int(x) for x in input("Please enter two int values:\n").split(",")]
    # print(a*b)
#   READ three float VALUES FROM KEYBOARD AND MULTIPY THEM


    # a,b,c=[float(x) for x in input("Please enter three flaot values:\n").split(',')]

    # print(a*b*c)#4,4.5,8.2-->147.6


#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS
#COMMAND LINE ARGUMENTS


# WE CAN USE CLA FOR TAKING INPUT WHILE COMILING THE CODE.
# COMMAND LINE ARG ARE ALWAYS OF TYPE OF STR TYPE ONLY.


# SYNTAX:
# argv-->present inside the sys module
# argv --> type(argv)#list


# from sys import argv
# l=[]
# for x in argv[1:]:
#     l.append(eval(x))
# print(l)
# # print(argv)
# # print(type(argv))


# OUTPUT STREAM
# FORM1:OS WITH NO ARG
    # print()
# FORM2:STRING ARG:
    # print("shyam verma is very nice guy and he is too simple")
    # print("shyam"+"verma")
    # print("shyam"*3)
    # print("shyam","verma","got ",100 )
    # a,b,c=1,3,5
# SEP OPERATOR:WE USE IT FOR SELECTING THE SEPRATOR BW TWO ARG OF PRINT()
    # print(a,b,c,sep="\n")
# END OPERATOR:
    # print("hi",end=" ")
    # print("shyam",end=" ")
    # print("verma",end=" ")

# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE

# # FORM5:PRINT FORMATED STRING
    # a,c=4,43
    # b="shyam"
    # print("%s %d" %(b,c))

    # s="fdk"
    # l=[3,32,232,234,1,"shtam"]
    # print("hi %s the list is %s" %(l[5],l))

# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE
# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE# NOTE 
# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# # FORM6: PRINT WITH {}
    # a,b,c=4,2,5
    # print("{} {} {}".format(a,b,c))
    # print("{1} {2} {1}".format(a,b,c))
    # print("{z} {x} {y}".format(x=a,y=b,z=c))



# NOTE # NOTE# NOTE# NOTE# NOTE# NOTE# NOTE
# FLOW CONTROL  
    # 1.CONDITIONAL STATEMENTS:
        # IF
        # ELSE
        # IF ELSE
        # IF ELIF ELSE
    # 2. ITERATIVE STATEMENTS:
        # FOR
        # WHILE
    # 3.TRANSFER STATEMENTS:
        # PASS
        # DEL
        # CONTINUE
        # BREAK


# 1.CONDITIONAL STATEMENTS:
    # a=4
    # b=3
    # if(a<b):
    #     print("a<b".format(b))
    # else:
    #     print("a>b {}".format(a))


    # name=input("Please enter your username :\n")
    # if (name=="shyam" or name=="Shyam"):
    #     print("hi shyam we welcomes you:")
    # else:
    #     print("Chala ja bsdk🤬😡🤬")


# write a program for find the biggest of two values given by user
    # a=None
    # b=None
    # a=int(input("Please enter a"))
    # b=int(input("Please enter b"))


    # if(a<b):
    #     print("a is smaller than b")
        
    # else:
    #     print("a is greater than b")











# WRITE A PROGRAM FOR printing the english word for the number entered by the user

    # n=int(input("Please enter a number bw 0 to 999\n"))

    # unit={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
    # tenth={2:"TWENTY",3:"THIRTY",4:"FOURTY",5:"FIFTY",6:"SIXTY",7:"SEVENTY",8:"EIGHGTY",9:"NINTY"}
    # exce={10:"TEN",11:"ELEVENT",12:"TWELVE",13:"THIRTEEN",14:"FOURTEEN",16:"SIXTEEN", 15:"FIFTEEN",17:"SEVENTEEN",18:"EIGHTEEN",19:"NINTEEN"}
    # if(n<10):
    #     print(unit[n])
    # elif(10<=n<=19):
    #     print(exce[n])
    # elif(n<100):
    #     unitplace=n%10
    #     tenthplace=n//10
    #     print(tenth[tenthplace],unit[unitplace])
    # elif(n<1000):
    #     unitplace=n%10
    #     tenthplace=(n//10)%10
    #     hundredthplace=int(n/100)
    #     print(unit[hundredthplace],"HUNDRED",tenth[tenthplace],unit[unitplace])


# ITERATIVE STATEMENTS:
    # for
    # while

# write a program for printint the each character present in the string.
    # s="shyam verma is very good guy"
    # for x in s:
    #     print(x,end=" ")

    # s="shyam"

    # if "s" in s:
    #     print("ss")








# ****************************************************************************************************  #

    # n = int(input("Please enter a nuber\n"))


    # unit=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINTEEN"]

    # ten=[" "," ","TWENTY","THIRTY","FOURTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINTY"]

    # if(n<20):
    #     print(unit[n])
    # elif(n<100):
    #     unitplace=n%10
    #     tenplace=n//10
    #     print(ten[tenplace],unit[unitplace])
    # elif(n<1000):
    #     unitplace=n%10
    #     tenplace=(n%100)//10
    #     hundredplace=n//100
    #     print(unit[hundredplace],"HUNDRED AND",ten[tenplace],unit[unitplace])
    # elif(n<19000):
    #     unitplace=n%10
    #     tenplace=(n%100)//10
    #     hundredplace=(n%1000)//100
    #     thousandplace=n//1000
    #     print(unit[thousandplace],"THOUSANDS",unit[hundredplace],"HUNDRED AND",ten[tenplace],unit[unitplace])
        

    #     # hundredplace=n%1000
    #     # thousandplace=n//1000
    #     # print(unit[hundredplace],ten[tenplace],unit[unitplace])

    # CALCULATE THE SUM OF ALL ELEMENTS PRESENT IN IN THE LIST.
        # l=[30,23,23]
        # su=0
        # for x in l:
        #     su=su+x
        # print(su)


# WHILE LOOP
# print numbers from 1 to 10 using while loop
    # x=1
    # while x<11:
    #     print(x)
    #     x+=1

# find the sum of the first n natural numbers

    # n=int(input("Please enter a number"))
    # i=1
    # sum=0
    # while i<=n:
    #     sum+=i
    #     i=i+1
    # print(sum)
# l="3,2,2,'1',4,2"
# s=[eval(x) for x in l.split()]
# print(s)
    # s="1 4 2 4 2 5 2 4"
    # r=[eval(x) for x in s.split()]
    # print(r)
    # r=[eval(x) for x in input("Please enter a nmbr").split()]
    # print(r)







#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE
#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE
#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE
#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE
#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE
#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE
#NOTE NOTE WHILE LOOP NOTE NOTE NOTE NOTE

    # while condition:
    #     body



#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE
#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE
#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE
#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE
#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE
#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE
#NOTE NOTE NOTE NOTE pattern programs NOTE NOTE NOTE NOTE



# n=int(input("Please enter a number"))

# print("* "*n)#will print n star in a row

# the below code will print star in n*n dimension
    # for i in range(n):
    #     for j in range(n):
    #         print("*",end=" ")
    #     print()

    #     # * * * * *
    #     # * * * * *
    #     # * * * * *
    #     # * * * * *
    #     # * * * * *

    # for i in range(n):
    #     print("* "*n)

    #     # * * * * *
    #     # * * * * *
    #     # * * * * *
    #     # * * * * *
    #     # * * * * *


    # for i in range(1,n+1):
    #     for j in range(n):
    #         print(i,end=" ")
    #     print()

    # # 1 1 1 1 1
    # # 2 2 2 2 2
    # # 3 3 3 3 3
    # # 4 4 4 4 4
    # # 5 5 5 5 5

    # for i in range(n):
    #     print((str(i+1)+" ")*n)

    # # # 1 1 1 1 1
    # # # 2 2 2 2 2
    # # # 3 3 3 3 3
    # # # 4 4 4 4 4
    # # # 5 5 5 5 5

    # a=65
    # for i in range(n):
        
    #     for j in range(n):
    #         print(chr(a),end=" ")
    #     print()
    #     a=a+1

    #     # A A A A A
    #     # B B B B B
    #     # C C C C C
    #     # D D D D D
    #     # E E E E E

    # for i in range(n):
    #     for j in range(n):
    #         print(j+1,end=" ")
    #     print()

    #     # Please enter a number5
    #     # 1 2 3 4 5
    #     # 1 2 3 4 5
    #     # 1 2 3 4 5
    #     # 1 2 3 4 5
    #     # 1 2 3 4 5

    # for i in range(n):
    #     for j in range(n,0,-1):
    #         print(j,end=" ")
    #     print()

    #     # 5 4 3 2 1
    #     # 5 4 3 2 1
    #     # 5 4 3 2 1
    #     # 5 4 3 2 1
    #     # 5 4 3 2 1


    # for i in range(n):
    #     for j in range(i+1):
    #         print("*",end=" ")
    #     print()


    #     # *
    #     # * *
    #     # * * *
    #     # * * * *
    #     # * * * * *

    # for i in range(n):
    #     print("* "*(i+1))


    #     # *
    #     # * *
    #     # * * *
    #     # * * * *
    #     # * * * * *

    # for i in range(n):
    #     for j in range(i+1):
    #         print(n-j,end=" ")
    #     print()



    #     # 5
    #     # 5 4
    #     # 5 4 3
    #     # 5 4 3 2
    #     # 5 4 3 2 1


    # for i in range(n):
    #     for j in range(n):
    #         if(n-i-1<=j):
    #             print("*",end=" ")
    #         else:
    #             print(" ",end="")
    #     print()


    # #     *
    # #    * *
    # #   * * *
    # #  * * * *
    # # * * * * *


    # for i in range(n):
    #     print(" " * (n-i-1),end="")
    #     print("* "*(i+1))



    # #     *
    # #    * *
    # #   * * * 
    # #  * * * *
    # # * * * * *

    # for i in range(n):
    #     # for j in range(n):
    #         print(" "*i,end="")
    #         print("* "*(n-i))

    #     # * * * * *
    #     #  * * * *
    #     #   * * *
    #     #    * *
    #     #     *





    # for i in range(n):
    #     for j in range(n):
    #         if(n-i-1==j or j==n-1):
    #             print("*",end=" ")
    #         elif(n-i-1<j and j<n-1):
    #             print("  ",end="")
    #         else:
    #             print(" ",end="")
    #     print()


    #     #     *
    #     #    * *
    #     #   *   *
    #     #  *     *
    #     # *       *



    # for i in range(n):
    #     for j in range(n):
    #         if(j>=i):
    #             print("* ",end="")
    #         else:
    #             print(" ",end="")
    #     print()


    #     # * * * * *
    #     #  * * * *
    #     #   * * *
    #     #    * *
    #     #     *


    # for i in range(n):
    #         for j in range(n):
    #             if(j==i or j==n-1):
    #                 print("* ",end="")
    #             elif(j>i and j<n-1):
    #                 print("  ",end="")
    #             else:
    #                 print(" ",end="")
    #         print()

    #     # *       *
    #     #  *     *
    #     #   *   *
    #     #    * *
    #     #     *








    # for i in range(n):
    #         for j in range(n):
    #             if(n-i-1==j or j==n-1):
    #                 print("*",end=" ")
    #             elif(n-i-1<j and j<n-1):
    #                 print("  ",end="")
    #             else:
    #                 print(" ",end="")
    #         print()
    # for i in range(n):
    #         for j in range(n):
    #             if(j==i or j==n-1):
    #                 print("* ",end="")
    #             elif(j>i and j<n-1):
    #                 print("  ",end="")
    #             else:
    #                 print(" ",end="")
    #         print()

    #     #     *
    #     #    * *
    #     #   *   *
    #     #  *     *
    #     # *       *
    #     # *       *
    #     #  *     *
    #     #   *   *
    #     #    * *
    #     #     *



# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# DIDN'T GET THE DIESIRED OUTPUT:
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # for i in range(n):
    #     for j in range(n-3):
    #         if((i==0 or i==(n//4)) and (j>0 or j<n-8)):
    #             print("* ",end="")
    #         if((j==0 or j==n-4) and (i!=0 or j!=n//4)):
    #             print("* ",end="")
    #         else:
    #             print("  ",end="")
    #     print()





    # # Please enter a number20
    # # * * *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # * * *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
    # # *                               *
                





# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# TRANSFER STATEMENTS:break , continue
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# transfer statements are used in the loop staements
# break: if condition falls: break the loop and come out from the loop
# continue: if condition falls: continue the loop for remaining itrations:




# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# cart=[10,20,30,60,40,70,50]
# # cart=[10,20,30,600,40,700,50]
# for item in cart:
#     if item>=500:
#         print("we can't place the order")
#         break;
#     print("processing item: {}".format(item))
# else:
#     # in this case else will always associated with only and only break statement
#     # else block will be executed only if foor loop executed without break statement
#     print("Congrats ... All your items processed successfully")












# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE
# pass pass pass pass pass pass pass
# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE


# pass is empty statement it doesn't do any thing
# we say to comiler that will devolep this part leter


    # if 10>5:
    #     print(true)
    #     pass
    # else:




# NOTE NOTE NOTE NOTE NOTE  NOTE
# del del del del del del del del del
# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE



# del is used for deleting the particular variable
# for i.e
# x=10
# x variable is pointing to the object <class int> 10
# del x
# print(x)#NameError: name 'x' is not defined
# s="shyam"
# del s[0]#TypeError: 'str' object doesn't support item deletion
# we can delete s but can't delete s[0]



# NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE
# DATA TYPE DATA TYPE DATA TYPE
# NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE

    # int 
    # str
    # bool
    # complex
    # float

    # list
    # tuple
    # set 
    # frozenset
    # bytes
    # bytearray

    # dict
    # None
    # range




# STRING NOTE

    # s="shyam"
    # print(s[0])#accessing the string member with the help of index
    # print(s[-1])#accessing the string member with the help of index
    # print(s[1:])#accessing the string member with  the help of slice operator.

# # wite a program to print the each character o the string with the help of indexing

    # s="shyam"
    # print("accessing all character present in the string with the help of positive indexing")
    # print()
    # i=0
    # while i<=len(s)-1:
    #     print("character at {} index is {}".format(i,s[i]))
    #     i+=1
    # print()
    # print()
    # print()
    # print("accessing all character present in the string with the help of negative indexing")
    # print()
    # i=-1
    # while (i+len(s)!=-1):
    #     print("character at {} index is {}".format(i,s[i]))
    #     i-=1
        
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# neagative index=positive index- len(string)
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE

    # s="shyam"
    # i=0
    # for x in s:
    #     print("the character at {} index and at {} index is: {} ".format(i,i-len(s),x))
    #     i+=1


# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# SLICE OPERATOR
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# string[begin:end:step]
# string[end:begin:step]

# s="shyam verma"
# print(s[::1])#shyam verma
# print(s[::-1])#amrev mayhs--> reverse of string with the help of slice operator
# print(s[::0])#ValueError: slice step cannot be zero
# print(s[3:5:-1])#empty string
# print(s[6:2:-1])#v ma
# print(s[0:10000:1])#shyam verma
# print(s[0:10000:-1])#empty string
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # print(s[-4:0:-1])#(s[-4]=e,s[0+1]=h)ev mayh
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# print(s[0:-5:-10])#empty string










# write a program to read string from the keyboard and print its character in both
# forward and backward direction(don't use the slice operator)

    # method 1:
    # n=input("Please enter any string")

    # i=0
    # print("In forward direction")
    # while i<len(n):
    #     print(n[i],end="")
    #     i+=1
    # i=-1
    # print()
    # print("In backward direction")
    # while i>=-(len(n)):
    #     print(n[i],end="")
    #     i-=1

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # method 2:
    # n=input("Please enter any string")
    # print("In forward direction")
    # for x in n:
    #     print(x)

    # print("In backward direction")
    # for x in n[::-1]:
    #     print(x)
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE



# comparison operator:
    # s1=input("Please enter 1st string")
    # s2=input("Please enter 2nd string")

    # if s1  == s2:
    #     print("Both strings are equal")
    # elif s1 < s2:
    #     print("s1 is less than s2")
    # else:
    #     print("s1 is greater than s2")

#HOW TO REMOVE THE SPACES FROM THE STRING
#HOW TO CONVERT THE STRING TO UPPER OR LOWER CASE


# city=input("Please enter your city name").strip().lower()

# if city=="zirnya":
#     print("or kya hal hai")
# elif city=="indor":
#     print("kaise ho")
# elif city== "bhopal":
#         print("Adab")
# else:
#     print("Please enter valid city")


# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# #About: This program is written to print that the particular character 
# # is present in the given string or not and print the occurences of the string.
# s="sahyaamavermaa"
# count=0
# pos=0
# while True:
#     if (s.find('a',pos,len(s))!=-1):
#         print("found at index {}".format(s.find('a',pos,len(s))))
#         pos=s.find('a',pos,len(s))+1
#         count+=1
#     else:
#         break
# print("'a' was present in the string %d times" %(count))

    #     #  found at index 1
    #     # found at index 4
    #     # found at index 5
    #     # found at index 7
    #     # found at index 12
    #     # found at index 13
    #     'a' was present in the string 6 times

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
#index()function
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# the functionalites of index method are same 
# as find methods the only different is that :
# when substring not found in the given string,
# it return -1 but index returns value error for the same
# 
# let's take an example:
    # s="shyam"
    # print(s.find('q'))#-1
    # print(s.index('q'))#ValueError: substring not found


# COUNTING SUBSTRING IN THE GIVEN STRING
    # string.count('subs')
    # string.count('subs',begin,end)



# write a program to find out the number of 
# white space present in the given string

    # s=input("Please enter a string\n")
    # s1=s.replace(" ","")
    # print(len(s)-len(s1))
    # print(s.count(" "))
# NOTE -> WE CAN ALSO USE THE COUNT FUNCTION FOR THE SAME
#seprate and join string
    # # seprate
    # s="shyam verma"
    # s1=s.split()
    # print(s1)#['shyam', 'verma']
    # print(type(s1))#<class 'list'>

    # # join
    # l=("shyam",'verma')
    # s=' '.join(l)
    # print(s)#shyam verma
    # print(type(s))#<class 'str'>


    # t=('10','20','30')
    # s=''.join(t)
    # print(s)#102030

# #changing case of string


    # s="shyam".upper()
    # print(s)
    # s="shyam".lower()
    # print(s)
    # s="shyam".capitalize()
    # print(s)
    # s="Shyam Verma".swapcase()
    # print(s)
    # s="shyam verma is a good guy".title()
    # print(s)

#  check the typee of charcter present in the string
    # # isalnum()->returns true if each character is either alphabate or number
    # print('durgaerw2323'.isalnum())#T
    # # isalpha()-> returns true if each character of string is only alphbate
    # print('dfsfsl4343'.isalpha())#F
    # # isdigit()-> returns true if each char is digit
    # print("334566".isdigit())#t
    # # islower()-->returns true if every alphabatic character char is in lower alphabate
    # print("334566".islower())#f
    # # isupper()-->returns true if every alphabatic character char is in upper alphabate
    # print("334566".isupper())#f
    # # istitle()--> returns true if every alphabatic character word start with upper case character of given string
    # print("334566".istitle())#f
    # # isspace()-->returns true if each character present in string is space only
    # print("    ".isspace())#t


    # s=input("enter any character")

    # if s.isalnum():
    #     print("alphanumeric string")
    #     if s.isalpha():
    #         print("alphbatic string")
    #         if s.islower():
    #             print("lower case string")
    #         else:
    #             print("lower case string")
    #     else:
    #         print("numeric string")
    # elif s.isspace():
    #     print("string content space only")
    # else:
    #     print("string content special symbols")



#startswith()-->returns true if string starts with substring
#endswith()-->returns true if string ends with substring

    # s="shyam verma and khushi"
    # print(s.startswith('s'))
    # print(s.endswith('s'))

s="the price of the product is ₹545"
i=s.find("₹")
i+=1
l=[]
print("₹",end="")
while True:
    if s[i:].isnumeric():
        l.append(s[i])
        print(s[i],end="")
        i+=1
    else:
        break
print()
num=''.join(l)
num=int(num)
print(num)
print(type(num))
print()

























# PRINT A:
    # n=int(input("Enter the value of n :- "))
    # # print(" *"*4,end='')
    # for i in range(n+1):
    #     for j in range(n):
    #         if(i==0):
    #             if(j>0 and j<=n-1):
    #                 print("*",end=" ")
    #             if(j==0):
    #                 print(" ",end="")
    #         elif(i==3):
    #             print("*",end=" ")
    #         elif((i>0 and j==0)or(i>0 and j==n-1)):
    #             print("*",end=" ")
    #         else:
    #             print("  ",end="")
    #     print()

# PRINT B:
    # n=int(input("Enter the value of n :- "))
    # for i in range(n):
    #     for j in range(n):
    #         if (i==n//2 or i==0 or i==n-1):
    #             if(0<=j<n-3):
    #                 print("*",end=" ")
    #             else:
    #                 print(" ",end=" ")
    #         elif(j==0 or j==n-3):
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()


# PRINT C:
    # n=int(input("Enter the value of n :- "))
    # for i in range(n):
    #     for j in range(n):
    #         if(i==0 or i==n-1):
    #             if(0<j<n-1):
    #                 print("*",end=" ")
    #             else:
    #                 print(" ",end=" ")
    #         elif(j==0):
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()

# PRINT D:
    # n=int(input("Enter the value of n :- "))
    # for i in range(n):
    #     for j in range(n):
    #         if(i==0 or i==n-1):
    #             if(0<=j<n-1):
    #                 print("*",end=" ")
    #             else:
    #                 print(" ",end=" ")
    #         elif(j==0 or (j==n-1 and 0<i<n-1)):
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()

# PRINT E:
    # n=int(input("Enter the value of n :- "))
    # for i in range(n):
    #     for j in range(n):
    #         if(i==0 or i==n//2 or i==n-1):
    #             # if(0<=j<n-1):
    #                 print("*",end=" ")
    #             # else:
    #                 # print(" ",end=" ")
    #         elif(j==0):
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()

# PRINT F:
# n=int(input("Enter the value of n :- "))
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i==n//2):
#             print("*",end=" ")
#         elif(j==0):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# PRINT O:
    # n=int(input("Enter the value of n :- "))
    # for i in range(n):
    #     for j in range(n):
    #         if(i==0 or i==n-1):
    #             if(0<j<n-1):
    #                 print("*",end=" ")
    #             else:
    #                 print(" ",end=" ")
    #         elif(j==0 or j==n-1):
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()

# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE
# GoToWebinar
# NOTE NOTE NOTE NOTE NOTE  NOTE
# NOTE NOTE NOTE NOTE NOTE  NOTE
