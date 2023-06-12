s=input("enter any character")

if s.isalnum():
    print("alphanumeric string")
    if s.isalpha():
        print("alphbatic string")
        if s.islower():
            print("lower case string")
        else:
            print("lower case string")
    else:
        print("numeric string")
elif s.isspace():
    print("string content space only")
else:
    print("string content special symbols")
