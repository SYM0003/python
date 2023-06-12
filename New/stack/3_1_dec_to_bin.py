from implimentation import Stack
def dtb(num):
    s=Stack()
    while(num>0):
        reminder=num%2
        num=num//2
        s.push(reminder)
    
    bin_str=''
    while not s.is_empty():
        bin_str+=str(s.pop())
    return bin_str

print(dtb(12))