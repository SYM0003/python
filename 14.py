def main():
    '''this is the main function'''
    num=5
    for i in range(1,num+1):
        if i%2!=0:
            count=1
        else:
            count=0
        for j in range(1,i+1):
            if count==1 :
                print(1,end=" ")
                count=0
            elif count==0:
                print(0,end=" ")
                count=1
        print()

if __name__=='__main__':
    main()
