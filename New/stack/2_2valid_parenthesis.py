from implimentation import Stack
def mathes(open,close):
    opens='({['
    closes=')}]'
    return opens.index(open) ==closes.index(close)
def par_checker(symbol_string):
    s=Stack()
    index=0
    balanced=True

    LEN=len(symbol_string)
    while index<LEN and balanced:
        symbol=symbol_string[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced=False
            else:
                top=s.pop()
                if not mathes(top, symbol):
                    balanced=False
                
                    
        index+=1
    return balanced and s.is_empty()



symbol_string=input('Enter the string')
print('valid') if par_checker(symbol_string) else print('Invalid')