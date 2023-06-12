from abc import ABC,abstractclassmethod
class abstactStack(ABC):  
    @abstractclassmethod
    def pop():
        pass
    @abstractclassmethod
    def top():
        pass
    @abstractclassmethod
    def push():
        pass
    @abstractclassmethod
    def is_empty():
        pass
    @abstractclassmethod
    def size():
        pass

    
class Stack:
    def __init__(self,stack=[]):
        self.stack=stack.copy()
    def size(self):
        return len(self.stack)
    def top(self):
        if(len(self.stack)==0):
            print('No element in stack')
            return
        return self.stack[-1]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack==[]


if __name__=='__main__':
    s=Stack()
    print(s.top())
