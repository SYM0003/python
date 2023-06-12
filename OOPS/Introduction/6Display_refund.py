'''
 How de we go about displaying the refund amount? One way is to recalculate the price as shown 
 below. Here, Price calculation logic is replaced in purchace as well as in return function. 
 This obvious is  a bad idea
'''
def return_mobile(price,brand):
    if(brand=="Apple"):
        discount=10;
    else:
        discount=5;
    total_price=price-price*discount/100

    print("Total refundable price of mobile is",total_price)
def retun_shoe(price,material):
    if(material=="leather"):
        tax=5
    else:
        tax=2;
    total_price=price+price*tax/100

    print("Total refundable price of shoe is",total_price)


retun_shoe(5000,"leather")
retun_shoe(5000,"None")
return_mobile(200000,"Apple")
