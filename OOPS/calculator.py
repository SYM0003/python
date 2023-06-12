# class Calculator:
#     def __init__(self,operation):
#         self.operation=operation
    
#     def getoperand(self,operand):
#         pass
        
    
# s1=Calculator("add")


# from  tkinter import *
# window=Toplevel()
# # window2=Tk()
# label1=Label(window,text='calculator',fg='black',bg='white',)
# label1.pack()


# button1=Button(window,text='1',padx='10',pady='10',)
# button2=Button(window,text='2',padx='10',pady='10')
# button3=Button(window,text='3',padx='10',pady='10')
# button4=Button(window,text='4',padx='10',pady='10')
# button5=Button(window,text='5',padx='10',pady='10')
# button6=Button(window,text='6',padx='10',pady='10')
# button7=Button(window,text='7',padx='10',pady='10')
# button9=Button(window,text='8',padx='10',pady='10')
# button8=Button(window,text='9',padx='10',pady='10')
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='left')
# button4.pack(side='bottom')
# button5.pack(side='bottom')
# button6.pack(side='bottom')
# button7.pack(side='right')
# button9.pack(side='right')
# button8.pack(side='right')
# window.mainloop()
# # window2.mainloop()




import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy())
button.pack(side=BOTTOM)
tk.mainloop()