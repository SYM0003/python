n=int(input())
for i in range(n):
    for j in range(n):
        if n-i>j:
            print(" ",end="")
        else:
            print("*",end=" ")
    print("")
for i in range(int(n/2)):
    if(n%2==0):
        print(" "*int(2*n/2),"**")
    else:
        print(" "*int((2*n/2+1)),"**")
    