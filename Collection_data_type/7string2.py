# strip()-->>this function is used when we want to remove 
# the space form the begining and from the end of tthe sring 
# there are 2 more function are also:
# lstrip()-->> will remove the space from left side of the string
# rstrip()-->> will remove the space from right side of the string
# NOTE: this function will not remove the white space form the middile of the string

city=input("Please enter your city name").strip()

if city=="Zirnya":
    print("or kya hal hai")
elif city=="Indor":
    print("kaise ho")
elif city== "Bhopal":
        print("Adab")
else:
    print("Please enter valid city")
    