from tkinter import *

root=Tk()
root.geometry("150x150")
operator=" "
def clickme(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def clrdisplay():
    global operator
    operator=" "
    text_Input.set(" ")
def equals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)

text_Input=StringVar()
e1=Entry(root,textvariable=text_Input)
e1.grid(columnspan=4) 
b1=Button(root,text="1",command=lambda:clickme(1))
b1.grid(row=1)
b2=Button(root,text="2",command=lambda:clickme(2))
b2.grid(row=1,column=1)
b3=Button(root,text="3",command=lambda:clickme(3))
b3.grid(row=1,column=2)
b4=Button(root,text="4",command=lambda:clickme(4))
b4.grid(row=1,column=3)
b5=Button(root,text="5",command=lambda:clickme(5))
b5.grid(row=2)
b6=Button(root,text="6",command=lambda:clickme(6))
b6.grid(row=2,column=1)
b7=Button(root,text="7",command=lambda:clickme(7))
b7.grid(row=2,column=2)
b8=Button(root,text="8",command=lambda:clickme(8))
b8.grid(row=2,column=3)
b9=Button(root,text="9",command=lambda:clickme(9))
b9.grid(row=3)
b10=Button(root,text="0",command=lambda:clickme(0))
b10.grid(row=3,column=1)
b11=Button(root,text="=",command=equals)
b11.grid(row=3,column=2)
b16=Button(root,text="C",command=clrdisplay)
b16.grid(row=3,column=3)
b12=Button(root,text="+",command=lambda:clickme("+"))
b12.grid(row=4)
b13=Button(root,text="-",command=lambda:clickme("-"))
b13.grid(row=4,column=1)
b14=Button(root,text="*",command=lambda:clickme("*"))
b14.grid(row=4,column=2)
b15=Button(root,text="/",command=lambda:clickme("/"))
b15.grid(row=4,column=3)
root.mainloop()
