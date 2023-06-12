from implimentation import Stack


def infixtoPostfix(expression):
    postfix=[]
    op_stack=Stack()
    prec={'*':3,'/':3,'+':2,'-':2,'(':1}
    
    for token in expression:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '123456789':
            postfix.append(token)
        elif token=='(':
            op_stack.push(token)
        elif token==')':
            top_token=op_stack.top()
            while (not op_stack.is_empty()) and  top_token!='(':
                postfix.append(top_token)
                top_token=op_stack.top()


        else:
            while (not op_stack.is_empty()) and prec[op_stack.top()]>=prec[token]:
                postfix.append(op_stack.pop())
            op_stack.push(token)
    

    while(not op_stack.is_empty()):
        postfix.append(op_stack.pop())
    
    return ''.join(postfix)
print(infixtoPostfix('((A*(C+D))+B)'))#acd+*b+
# print(infixtoPostfix('((((A+B)*C)-(D-E))*(F+G))'))   #ab+c*de--fg+*