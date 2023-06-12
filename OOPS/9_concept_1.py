'''
accessing the member of 1 class into another class
has a relation

'''

class Employee:
    '''
    emloyee class
    '''
    def __init__(self,name,emp_id,salary):
        '''
        constructor
        '''
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        '''
        display mehtod
        '''
        print(f"Hi {self.name} !")
        print(f"your id is {self.emp_id}")
        print(f"your current salary is {self.salary}")


class Manager:
    '''
    manager class
    Here i'm using the employee class members
    '''
    @staticmethod
    def update(emp):
        '''
        updates the value of Employee.salary
        '''
        emp.salary+=50000
        #salary is the member of employee class but we are accessing it 
        # inside of the manager class
        print(f"congratulations {emp.name} now you are a manager of the company")



def main():
    '''
    This is the main function
    '''
    emp1=Employee('Shyam', '00234', 300000)
    emp1.display()
    Manager.update(emp1)
    print(emp1.salary)
if __name__=='__main__':
    main()
