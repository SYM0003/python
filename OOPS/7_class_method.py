''' program to demonstrate the class method of a class'''
class Student:
    '''student class to access student data'''
    college='SVCE'
    def set_rollno(self,roll_no):
        '''takes roll no and asign to the student'''
        self.roll_no=roll_no
    def set_name(self,name):
        ''' takes name and asign to the student'''
        self.name=name
    def get_name(self):
        '''print the name of the student'''
        print('The name of the student  is {}'.format(self.name))
    def get_roll_no(self):
        '''print the roll no of the student'''
        print('The roll number of the student  is {}'.format(self.roll_no))
    @classmethod
    def get_college(cls):
        '''static method'''
        print('The student belongs from {} college'.format(cls.college))

def main():
    '''mainn function'''
    student1=Student()
    name=input('Enter the name of the student')
    roll_no=input('Enter the roll No. of the student')
    student1.set_name(name)
    student1.set_rollno(roll_no)

    student1.get_name()
    student1.get_roll_no()
    Student.get_college()

if __name__=='__main__':
    main()
