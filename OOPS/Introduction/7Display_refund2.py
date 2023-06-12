'''
Alternatively we can use global variable. 
We  calculate the price during purchace and store it in global variable.
Later during return we will access the calculated price from the golobal variable.
But this brings more complications, that it tries to solve.
'''
total_price_mobile=0 
total_price_shoe =0

def purchase_mobile(brand, price):
    if(brand=="Apple"):
        discount=10
    else:
        discount=5
    total_price_mobile=price-price*discount/100
    print("Total price of Mobile is "+str(total_price_mobile))
def purchase_shoe(material,price):
    if(material=="leather"):
        tax=5
    else:
        tax=2
    total_price_shoe=price+price*tax/100
    print("Total price of Shoe is "+ str(total_price_shoe))

def return_mobile():
    print("The total refundable price is "+str(total_price_mobile))

def return_shoe():
    print("The total refundable price is "+str(total_price_shoe))


purchase_mobile("Apple",200000)
purchase_shoe("leather",2000)
return_shoe()