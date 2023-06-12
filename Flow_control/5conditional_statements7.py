# Author: shyam verma
# About: This program is written for printing the english word for the number given by the user.
# this program is written to print the word form of a number entered by the user from range 0 to 9999 
n=int(input("Please enter a number bw 0 to 999\n"))
unit={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",10:"TEN",11:"ELEVENT",12:"TWELVE",13:"THIRTEEN",14:"FOURTEEN",16:"SIXTEEN", 15:"FIFTEEN",17:"SEVENTEEN",18:"EIGHTEEN",19:"NINTEEN"}
tenth={1:"TEN",2:"TWENTY",3:"THIRTY",4:"FOURTY",5:"FIFTY",6:"SIXTY",7:"SEVENTY",8:"EIGHGTY",9:"NINTY"}
unitplace=n%10
tenhplace=(n%100)//10
hundredplace=(n%1000)//100
thousandplace=(n%10000)//1000
# tenthousandplace=(n%100000)//10000
if(thousandplace != 0):#taaa
    if(hundredplace !=0):#thaa
        if(tenhplace!=0):#thea
            if(tenhplace == 1):
                tenhplace=(tenhplace*10)+unitplace
                print(unit[thousandplace],"THOUSAND",unit[hundredplace],"HUNDRED AND",unit[tenhplace])
            else:
                if(unitplace != 0):#theu
                    print(unit[thousandplace],"THOUSAND",unit[hundredplace],"HUNDRED AND",tenth[tenhplace],unit[unitplace])
                else:#the0 1230
                    print(unit[thousandplace],"THOUSAND",unit[hundredplace],"HUNDRED AND",tenth[tenhplace])       
        else:#th0u
            if(unitplace != 0):#th0u
                print(unit[thousandplace],"THOUSAND",unit[hundredplace],"HUNDRED AND",unit[unitplace])
            else:#th00
                print(unit[thousandplace],"THOUSAND",unit[hundredplace],"HUNDRED")
    # NOTE NOTE NOTE ALL DONE ALL DONE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    else:#t0eu
    # NOTE NOTE NOTE LET ME CHECK NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
        if(tenhplace!=0):#thea
            if(tenhplace == 1):
                tenhplace=(tenhplace*10)+unitplace
                print(unit[thousandplace],"THOUSAND",unit[tenhplace])
            else:
                if(unitplace != 0):#theu
                    print(unit[thousandplace],"THOUSAND",tenth[tenhplace],unit[unitplace])
                else:#the0 1230
                    print(unit[thousandplace],"THOUSAND",tenth[tenhplace])       
        else:#th0u
            if(unitplace != 0):#th0u
                print(unit[thousandplace],"THOUSAND",unit[unitplace])
            else:#th00
                print(unit[thousandplace],"THOUSAND")
    # NOTE NOTE NOTE LET ME CHECK NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
else:


    if(hundredplace !=0):#thaa
        if(tenhplace!=0):#thea
            if(tenhplace == 1):
                tenhplace=(tenhplace*10)+unitplace
                print(unit[hundredplace],"HUNDRED AND",unit[tenhplace])
            else:
                if(unitplace != 0):#theu
                    print(unit[hundredplace],"HUNDRED AND",tenth[tenhplace],unit[unitplace])
                else:#the0 1230
                    print(unit[hundredplace],"HUNDRED AND",tenth[tenhplace])       
        else:#th0u
            if(unitplace != 0):#th0u
                print(unit[hundredplace],"HUNDRED AND",unit[unitplace])
            else:#th00
                print(unit[hundredplace],"HUNDRED")
    # NOTE NOTE NOTE ALL DONE ALL DONE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    else:#t0eu
    # NOTE NOTE NOTE LET ME CHECK NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
        if(tenhplace!=0):#thea
            if(tenhplace == 1):
                tenhplace=(tenhplace*10)+unitplace
                print(unit[tenhplace])
            else:
                if(unitplace != 0):#theu
                    print(tenth[tenhplace],unit[unitplace])
                else:#the0 1230
                    print(tenth[tenhplace])       
        else:#th0u
            if(unitplace != 0):#th0u
                print(unit[unitplace])
            else:#th00
                print("THOUSAND")
    # NOTE NOTE NOTE LET ME CHECK NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE








    # if(hundredplace !=0):#@1@@
    #     if(tenhplace>1):#@12@
    #         if(unitplace != 0):#@12@
    #             print(unit[hundredplace],"HUNDRED AND",tenth[tenhplace],unit[unitplace])
    #         else:#@120
    #             print(unit[hundredplace],"HUNDRED AND",tenth[tenhplace])
    #     else:#@@1@  @@0@
    #         if(unitplace != 0):
    #             print(unit[hundredplace],"HUNDRED AND",unit[tenhplace])
    #         else:
    #             print(unit[hundredplace],"HUNDRED AND",unit[tenhplace])

    # else:
    #     if(tenhplace>1):
    #         if(unitplace != 0):
    #             print(tenth[tenhplace],unit[unitplace])
    #         else:
    #             print(tenth[tenhplace])
    #     else:
    #             print(unit[unitplace])
































































# if(n<20):
#     print(unit[n])
# elif(n<100):
#     unitplace=n%10
#     tenthplace=n//10
#     print(tenth[tenthplace],unit[unitplace])
# elif(n<1000):
#     unitplace=n%10
#     tenthplace=(n//10)%10
#     hundredthplace=int(n/100)
#     print(unit[hundredthplace],"HUNDRED",tenth[tenthplace],unit[unitplace])

# else:
#     print("Please enter number bw 0 to 999")
# # 1589647
