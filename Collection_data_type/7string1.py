
# write a program to read string from the keyboard and print its character in both
# forward and backward direction(don't use the slice operator)

    # method 1:
    # n=input("Please enter any string")

    # i=0
    # print("In forward direction")
    # while i<len(n):
    #     print(n[i],end="")
    #     i+=1
    # i=-1
    # print()
    # print("In backward direction")
    # while i>=-(len(n)):
    #     print(n[i],end="")
    #     i-=1

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# method 2:
n=input("Please enter any string")
print("In forward direction")
for x in n:
    print(x)

print("In backward direction")
for x in n[::-1]:
    print(x)
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE