'''
Problem:-The modified code would look something like this:
'''
def purchase_mobile(Brand,price):
    if(Brand=="Apple"):
        discount=10
    else:
        discount=5
    total_price=price-price*discount/100
    print("Total price of Mobile is", total_price)
def purchase_shoe(material,price):
    if(material=="leather"):
        tax=5
    else:
        tax=2
    total_price=price+price*tax/100
    print("Total price of Shoe is", total_price)


purchase_mobile("Apple",200000)
purchase_shoe("leather",2000)