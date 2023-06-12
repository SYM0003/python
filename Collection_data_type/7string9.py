# write a program to reverse given string
s='shyam'
# METHOD 1:
# s='shyam'
    # i=-1
    # while True:
    #     if i!=(-len(s)-1):
    #         print(s[i],end="")
    #         i-=1
    #     else:
    #         break
# NOTE: WE CAN ALSO USE STRING CONCATENATION. HOW? 
    # s='shyam'
    # i=len(s)-1
    # output=''
    # while i>=0:
    #     output=output+s[i]
    #     i-=1
    # print(output)



# METHOD 2:
    # s='shyam'
    # print(s[::-1])#mayhs
    # print(s[-1:-len(s)-1:-1])#mayhs
    

# METHOD 3:
# with the help of reversed() function: it returns the list of character of string
# for example:
# i have string s='shyam'
# then it will return a list as below: ['m','a','y','h','s'] 
# so we can use join() function and it will return the reverse of 
# the string
    # s='shyam'
    # r=reversed(s)
    # reverse_s=''.join(r)
    # print(reverse_s)#'mayhs'







# REVERSE THE ORDER OF WORDS OF THE STIRNG
# METHOD 1:
    # s="shyam verma is very good guy"
    # s_w_r_l=s.split(' ')
    # s_w_r=' '.join(s_w_r_l[::-1])
    # print(s_w_r)#guy good very is verma shyam

# METHOD 2:
    # s="shyam verma is very good guy"
    # l=['']
    # i=0
    # for x in s:
    #     if x!=' ':
    #         l[i]=l[i]+x
    #     else:
    #         l.append('')
    #         i+=1
    # s_w_r=' '.join(l[::-1])
    # print(s_w_r)#guy good very is verma shyam


# METHOD 3:
    # s="shyam verma is very good guy"
    # l=s.split()
    # i=len(l)-1
    # l1=[]
    # while i>=0:
    #     l1.append(l[i])
    #     i-=1
    # reverse_s=' '.join(l1)
    # print(reverse_s)







# REVERSE THE INTERNAL CONTENT OF THE WORDS AND ORDER OF 
# THE WORDS SHOULD REMAIN SAME
#  METHOD 1:
    # s="shyam verma is very good guy"
    # l=s.split()
    # i=0
    # n=len(l)
    # l1=[]
    # while i<n:
    #     l1.append(l[i][::-1])
    #     i+=1
    # output=' '.join(l1)
    # print(output)


# PRINT THE REVERSED ORDER OF INTERNAL WORDS OF GIVEN STRING AND ONLY PRINT THE WORD
# WHICH ARE PRESENT AT EVEN INDEX
    # s="shyam verma is very good guy"
    # l=s.split()
    # i=0
    # l1=[]

    # for i in range(len(l)):
    #     if (i+1)%2==0:
    #         l1.append(l[i][::-1])
    # print(l1)
    # output=' '.join(l1)
    # print(output)


# PRINT THE CHARACTER OF STRING THAT ARE PRESENT AT ODD POSTINON
# MEHTOD 1:
    # s="shyam verma is very good guy"

    # print(s[::2])#symvrai eygo u
    # s='shyam'
    # print(s[::2])#sym


# METHOD 2: WITHOUT USING SLICE OPERATOR
    # s="shyam verma is very good guy"

    # for i in range(len(s)):

    #     if i%2==0:
    #         print(s[i],end='')#symvrai eygo u
    # s='shyam'
    # print()
    # for i in range(0,len(s),2):
    #     print(s[i],end='')#sym


# WRITE A PROGRAM TO JOIN THE CHARACTER OF TWO STRIN IN A SING
# LE STRING AND TAKE THAT 
    # s1='shyam'
    # s2='khushi'
    # s3=''
    # i=len(s1)
    # j=len(s2)
    # k=0
    # while True:
    #     if(k<len(s1)):
    #         s3=s3+s1[k]
    #     if(k<len(s2)):
    #         s3=s3+s2[k]
    #     k+=1
    #     if(k>=len(s1) and k>=len(s2)):
    #         break
    # print(s3)
    


#WAP TO SORT CHARCTER PRSENT IN THE GIVEN STRING. FIRST ALPHABATE SYMBOL AND THEN NUMERIC VALUES


    # s='S3DIFI1WE5RFK243249'
    # s1=s2=''

    # for x in s:
    #     if x.isalpha():
    #         s1=s1+x
    #     else:
    #         s2=s2+x

    # output=''
    # output=output+(''.join(sorted(s1)))+(''.join(sorted(s2)))
    # print(output)#DEFFIIKRSW122334459



# WAP FOR FOLLOWINT REQUIREMENT
    # # input='a2b3c4'

    # # output='aabbbcccc'


    # # s='g5hr2ffs5e'-->test case

    # # s=input("please enter an alphnumberic string\n")
    # s='jfgr2gh6hh2,g23'#-->test case
    # s=s+' '
    # i=0
    # output=''
    # while i<len(s):
    #         if s[i].isspace():
    #             break
    #         if s[i+1].isnumeric():
    #             output=output+(s[i]*int(s[i+1]))
    #             i+=2
    #         else:
    #             output=output+s[i]
    #             i+=1
    # print(output)
    # # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE THIS PROGRAM HAS A BUG THAT IF WE PASS STRING
    # # LIKE BELOW 'jfgr2gh6hh2,g23' THEN IT SHOULD PRINT THE LAST g for 23 time but 
    # # it print the g only for 2 time so i have to find the solutionn for the same
    # # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    # # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
                
# i have fixed the bug which was discribed in above note 
# this block of code can work for all that situations
# 
    # # s='jfgr2gh06hh2,g10'#-->test case 0
    # s=input("please enter an alphnumberic string(please enter the string without space)\n")
    # s=s+' '
    # i=0
    # output=''
    # while i<len(s):
    #         if s[i].isspace():
    #             break
    #         if s[i+1].isnumeric():
    #             n=i+1
    #             cnt=1
    #             num=[]
    #             while s[n].isnumeric():
    #                 num.append(s[n])
    #                 n+=1
    #                 cnt+=1
    #             num=int(''.join(num))

    #             output=output+(s[i]*num)
    #             i+=cnt
    #         else:
    #             output=output+s[i]
    #             i+=1
    # print(output)










# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # MOTE SIMPLIFIED VERSION OF THE PROGRAM
# # i didn't get that example 

# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# # NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

    # s=input("enter any string\n")
    # i=0
    # num=''
    # output=''
    # while i<len(s):
    #     if s[i].isalpha():
    #         ch=s[i]
    #     else:
    #         num=num+s[i]
    #         if i==len(s)-1:
    #             output=output+ch*int(num)
    #         if i+1<len(s) and s[i+1].isalpha():
    #             output=output+ch*int(num)
    #             num=''
    #     i=i+1
    # print(output)





# input:a2b4c2
# output:acbgce
    # s=input('Please enter the string in format :"a2b4c2"')
    # i=0
    # temp=0
    # len_s=len(s)
    # while i<len_s:
    #     if(s[i].isalpha()):
    #         print(s[i],end='')
    #         temp=ord(s[i])
    #     else:
    #         temp+=in t(s[i])
    #         print(chr(temp),end='')
    #         temp=0
    #     i+=1




# WAP FOR REMOVING THE DUPLICATES FROM THE GIVEN STRING

    # s=input('Please enter the string ')
    # l=[]

    # for x in s:
    #     if x not in l:
    #         l.append(x)
    # output=''.join(l)

    # print(output)


# WAP FOR FIND THE NUMBER OF OCCURENCES IN FOR EACH CHARACTER IN THE STRING:

    # # method 1:
    # s=input('Please enter the string')
    # d={}

    # for x in s:
        
    #     if x not in d:
    #         d[x]=1
    #     else:
    #         d[x]=d[x]+1

    # for k,v in d.items():
    #     print("number of occureces of {} is: {}".format(k,v))

    # # method 2:
    # s=input('Please enter the string')
    # l=[]
    # for x in s:
    #     l.append(x)
    # output=sorted(l)#ddfhss
    # ch=''
    # cnt=0
    # for x in output:
    #     if ch!=x:
    #         print("number of occureces of ",ch ,"is:",cnt)
    #         ch=x
    #         cnt=1
    #     else:
    #         cnt+=1
    # print("number of occureces of ",ch ,"is:",cnt)
    




    
















