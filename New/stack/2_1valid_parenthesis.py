from implimentation import Stack

def par_checker(symbol_string):
    s=Stack()
    index=0
    balanced=True

    LEN=len(symbol_string)
    while index<LEN and balanced:
        symblol=symbol_string[index]
        if symblol=='(':
            s.push('(')
        else:
            if s.is_empty():
                balanced=False
            else:
                s.pop()
        index+=1
    return balanced and s.is_empty()



symbol_string=input('Enter the string')
print('valid') if par_checker(symbol_string) else print('Invalid')