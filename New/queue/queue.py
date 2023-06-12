class Queue:
    def __init__(self):
        self.item=[]
    def is_impty(self):
        return self.item==[]
    def enqueue(self,val):
        self.item.insert(0,val)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)


t=Queue()
print(f'the queue is {t.is_impty()}')
print(f'size of queue is {t.size()}')
t.enqueue(6)
print(f' the queue is {t.is_impty()}')
print(f'size of queue is {t.size()}')
t.enqueue(5)
print(f' the queue is {t.is_impty()}')
print(f'size of queue is {t.size()}')

print(t.item)

