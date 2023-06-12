#print some of first n numbers using while loops
n=int(input("Please enter the last number:"))
sum=0
sum1=0
x=n
while(x!=0):
    sum=sum+x;
    
    x-=1
sum1=n*(n+1)/2
print("The sum of first ",n," numbers is: ",sum)
print("The sum of first ",n," numbers is: ",sum1)