'''Proble 3:-
The solution we came up with has a key problem. Data for mobiles and shoes
are mixed up in the same code.
If we have to make change to the logic for purchasing shoe, we have to modify 
method that has logic for both shoes and mobiles. For example, if we have to add 
'material' to the shoe and have 5% tax on 'leather' shoes, then we have to go through
code related to mobile as well, as shown below: 
problem 4:-
A better solution would be to modularize the code and separate the logic for 
Mobiles and Shoes.Modify the code in the below code pane as 
per the following guidelines:
Create two functions: purchase_mobile and purchase_shoe
purchase_mobile() takes two parameters: price and brand
purchase_shoe() takes two parameters: price and material
If the mobile brand is “Apple”, discount is 10%, else discount is 5%
If the shoe material is “leather”, tax is 5%, else tax is 2%
'''
def purchase_product(product_type, price,Mobile_brand=None, material=None):
    if product_type == "Mobile":
        if Mobile_brand == "Apple":
            discount = 10
        else:
            discount =5
        total_price = price-price*discount/100
    else:
        if material == "leather":
            tax = 5
        else:
            tax = 2
        total_price = price+price*2/100

    print("Total Price of " + product_type + " is ",total_price)
        
purchase_product ("Mobile", 300000, "Apple", None)
purchase_product ("Shoe", 3000,  "leather")