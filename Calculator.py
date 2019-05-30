from tkinter import *
from tkinter.ttk import *
exp=""
def press(num):
     global exp
     exp=exp+str(num)
     equation.set(exp)

def equal():
    global exp
    res = eval(exp)
    exp = str(res)
    equation.set(res)

def clr():
    global exp
    exp = ""
    equation.set(exp)

window = Tk()
window.title("SIMPLE CALCULATOR")
window.configure(background = "light grey")
window.geometry('305x165')

#Label
lbl = Label(window, text = "SIMPLE CALCULATOR", font = ("Helvetica", "20", "bold italic"))
lbl.grid(columnspan = 4, row = 0)

#Display Screen
equation = StringVar()
display = Entry(window, width = 10, textvariable = equation)
display.focus()
display.grid(column = 0, row = 1)

#BUTTON / AND %

btnd = Button(window, text = "/", command = lambda:press('/'))
btnd.grid(column = 3, row = 1)

btnd = Button(window, text = "%", command = lambda:press('%'))
btnd.grid(column = 2, row = 1)

#BUTTON 7, 8, 9 AND *
btn7 = Button(window, text = "7", command = lambda:press(7))
btn7.grid(column = 0, row = 2)

btn8 = Button(window, text = "8", command = lambda:press(8))
btn8.grid(column = 1, row = 2)

btn9 = Button(window, text = "9", command = lambda:press(9))
btn9.grid(column = 2, row = 2)

btnm = Button(window, text = "*", command = lambda:press('*'))
btnm.grid(column = 3, row = 2)

#BUTTON 4, 5, 6 AND -

btn4 = Button(window, text = "4", command = lambda:press(4))
btn4.grid(column = 0, row = 3)

btn5 = Button(window, text = "5", command = lambda:press(5))
btn5.grid(column = 1, row = 3)

btn6 = Button(window, text = "6", command = lambda:press(6))
btn6.grid(column = 2, row = 3)

btns = Button(window, text = "-", command = lambda:press('-'))
btns.grid(column = 3, row = 3)

#BUTTON 1, 2, 3 AND +

btn1 = Button(window, text = "1", command = lambda:press(1))
btn1.grid(column = 0, row = 4)

btn2 = Button(window, text = "2", command = lambda:press(2))
btn2.grid(column = 1, row = 4)

btn3 = Button(window, text = "3", command = lambda:press(3))
btn3.grid(column = 2, row = 4)

btna = Button(window, text = "+", command = lambda:press('+'))
btna.grid(column = 3, row = 4)

#BUTTON CLR, 0, . AND =

btnc = Button(window, text = "CLR", command = clr)
btnc.grid(column = 0, row = 5)

btn0 = Button(window, text = "0", command = lambda:press(0))
btn0.grid(column = 1, row = 5)

btnp = Button(window, text = ".", command = lambda:press('.'))
btnp.grid(column = 2, row = 5)

btne = Button(window, text = "=", command = equal)
btne.grid(column = 3, row = 5)

window.mainloop()
