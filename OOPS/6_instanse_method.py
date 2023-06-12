''' instase method demonstration'''
class Student:
    '''student class for creating a student objecst'''
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    # instanse method:  first arg to the method is a reffrence to the
    #                   current obj whichi is passed by the pvm we don't
    #                   need to pass it explictly
    def get_data(self):
        ''' method to get the obj of particular obj'''
        print(self.name)
        print(self.roll_no)

def main():
    '''this is the main function'''
    student1=Student('Shyam', 54)
    student1.get_data()

if __name__=='__main__':
    main()
    