from implimentation import Stack
def base_converter(num,base):
    digits = "0123456789ABCDEF"
    s=Stack()
    while(num>0):
        reminder=num%base
        num=num//base
        s.push(reminder)
    
    bin_str=''
    while not s.is_empty():
        bin_str+=digits[s.pop()]
    return bin_str

print(base_converter(256,16))