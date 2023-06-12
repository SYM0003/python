class Student:
    def __init__(self,n,s,c):#->constructor
        '''n=name,s=scl name,c=clg name'''
        self.name=n
        self.school=s
        self.clg=c
    def show(self):#->method
        print("student name is {}".format(self.name))
        print("The school of {} was {}".format(self.name,self.school))
        print("The college of {} is {}".format(self.name,self.clg))


s=Student('shyam', "ASN zirnya", 'SVCE Indore')
s.show()