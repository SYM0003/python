'''Proble:-
Let us say we want to update our code such that:
1 If the mobile brand is Apple then the discount is 10% else the discount is 5%
2 All shoe have 2% discount and no discount.
'''
def purchase_product(product_type, price,Mobile_brand=None):
    if product_type == "Mobile":
        if Mobile_brand == "Apple":
            discount = 10
            total_price = price-price*discount/100
        else:
            discount =5
            total_price = price-price*discount/100
    else:

            total_price = price+price*2/100



    print("Total Price of " + product_type + " is ",total_price)
        
purchase_product ("Mobile", 30000, "Apple")
purchase_product ("Shoe", 2000)