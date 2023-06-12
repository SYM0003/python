'''Proble:-
consider the below code which allow you to purchase diffrent product.All product have discount of
10%. Run the below code and observe the output'''
def purchase_product(product_type, price):
    discount = 10
    total_price = price-price*discount/100
    print("Total Price of " + product_type + " is ",total_price)
        
purchase_product ("Mobile", 30000)
purchase_product ("Shoe", 2000)