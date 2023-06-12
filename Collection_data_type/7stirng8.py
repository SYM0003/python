#about:
    # THIS PROGRAM IS WRITTEN TO FETCH THE NUMBER FROM THE STRING
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