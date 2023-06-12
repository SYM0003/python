n=int(input("Please enter a number bw 0 to 99\n"))

unit={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
tenth={2:"TWENTY",3:"THIRTY",4:"FOURTY",5:"FIFTY",6:"SIXTY",7:"SEVENTY",8:"EIGHGTY",9:"NINTY"}
exce={10:"TEN",11:"ELEVENT",12:"TWELVE",13:"THIRTEEN",14:"FOURTEEN",16:"SIXTEEN", 15:"FIFTEEN",17:"SEVENTEEN",18:"EIGHTEEN",19:"NINTEEN"}




if(n<10):
    print(unit[n])
elif(10<=n<=19):
    print(exce[n])
else:
    unitplace=n%10
    tenthplace=n//10
    print(tenth[tenthplace],unit[unitplace])