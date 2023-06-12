'''
has a relation in python is a aproach of accessing members
of one class inside another class 
'''
# suppose we have to class name car and engine
# car--> a class defining the features/functionality of car
# engine->a class defining the features/functionality of engine

# now we can observe that each car must have a engine so it means 
# the car object will always have an engine
# so car has a engine reffrence
# we will use engine object inside of the car class it is called NOTE has a relation
# NOTE # has a relation ----->coposition,agregation


# # ei1
# class Engine:
#     def __init__(self):
#         self.power='123Kw'
#         self.type='Hybrid'
#     def use_engine(self):
#         print(f'Using engine of power {self.power} it is {self.type} engine')
# class Car:
#     def __init__(self,name):
#         self.name=name
#         self.engine=Engine()
#     def info (self):
#         print(f'The name of the car is {self.name}')
#         print(f'It has the engine of {self.engine.power} power')
#         print(f'engine is a "{self.engine.type}" engine')

# def main():
#     car=Car("BMW")
#     car.info()
# if __name__=="__main__":
#     main()

# # ei12 car and engine(agregation)
# class Car:
#     def __init__(self,name):
#         self.name=name
#         self.engine=self.Engine()
#     class Engine:
#         def __init__(self):
#             self.power='123Kw'
#             self.type='Hybrid'
#         def use_engine(self):
#             print(f'Using engine of power {self.power} it is {self.type} engine')
#     def info (self):
#         print(f'The name of the car is {self.name}')
#         print(f'It has the engine of {self.engine.power} power')
#         print(f'engine is a "{self.engine.type}" engine')

# def main():
#     car=Car("BMW")
#     car.info()
# if __name__=="__main__":
#     main()









# # ei2 employee and car

# class SportsNews:
#     def sports():
#         print('sports News 1')
#         print('sports News 3')
#         print('sports News 2')
# class politicsNews:
#     def politics():
#         print('Politics News 1')
#         print('Politics News 3')
#         print('Politics News 2')
# class BollywoodNews:
#     def bollywood():
#         print('Bollywood News 1')
#         print('Bollywood News 3')
#         print('Bollywood News 2')
# class News:
#     # def displayNews(politics,sports,bollywood):
#     def displayNews():
#         politicsNews.politics()
#         SportsNews.sports()
#         BollywoodNews.bollywood()


# def main():
#     politics=politicsNews()
#     sports=SportsNews()
#     bollywood=BollywoodNews()
#     News.displayNews()
#     # News.displayNews(politics, sports, bollywood)

# if __name__=="__main__":
#     main()
# 


# ei3 employee and car

class Car:
    def __init__(self,name,model,engine):
        self.name=name
        self.model=model
        self.engine=engine
    
    def display(self):
        print(f'The name of the car: {self.name}')
        print(f'The model of the car: {self.model}')
        print(f'Engine type is: {self.engine}')

class Employee:
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
        self.car=None
    def buy_car(self,car):
        self.car=car#->using car class object here
    def has_car(self):
        if self.car ==None:
            print(f"{self.name} doesn't has car")
        else:
            print(f'{self.name} has a car')
            self.car.display()#using method of car class

def main():
    employee1=Employee('shyam', 'e2321', 2332420)
    employee1.buy_car(Car("BMW", 'PTA NAHI', 'pTA NAHI'))
    employee1.has_car()
    employee2=Employee('Rohan', 'e2421', 233220)
    employee2.has_car()

if __name__=='__main__':
    main()



