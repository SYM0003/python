'''
    static method are the method which are created inside the
    class for fullfull the business requirements,it does not take 
    self variable or cls variable as argument
'''

class Student:
    def __init__(self,name,semester,
                 roll_no):
        self.name=name
        self.roll_no=roll_no
        self.semester=semester
    
    def get_semester(self):
        ''' prints the semester whome student belongs'''
        print('Semeseter:',self.semester)
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
    @staticmethod
    def get_total_student(student):
        '''this is the static method'''
        print('Total student : ',studnet)

def main():
    stdnt=Student('shyam', '6th', '54')

if __name__=='__main__':
    main()