'''
inner class and nested class
'''


class Car:
    def __init__(self,name,model,type,power):
        self.engine=self.Engine(type,power)
        self.name=name
        self.model=model
    def info(self):
        print('Showing info of the car')
        print(f'Model {self.name}')
        print(f'Moder {self.model}')
        print()
        self.engine.info()

    class Engine:
        def __init__(self,type,power):
            self.type=type
            self.power=power
        
        def info(self):
            print('Enfo of the Engine')
            print(f'type : {self.type}')
            print(f'power {self.power}')

def main():
    c=Car('BMW', '6R', 'HYBRID', '1000CC')
    c.info()

if __name__=='__main__':
    main()