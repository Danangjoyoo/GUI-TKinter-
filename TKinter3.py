from tkinter import *

root = Tk()
root.title("SIMPLE CALCULATOR")

var = IntVar()
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx= 10, pady = 10)
sign = ''

def cvtInt(value):
    fnum = []
    newnum = ''
    for i in value:
        ii = int(i)
        fnum.append(ii)
    for i in fnum:
        newnum = newnum + str(i)
    new = int(newnum)
    return new

def button_add(Number):
    current = e.get()
    length_current = len(current)
    e.insert(0+length_current, Number)

def button_clear():
    e.delete(0, END)

def button_equal():
    second_num = cvtInt(e.get())
    summit = 0
    if sign == '+':
        summit = first_num + second_num
        print('plus')
    elif sign == '-':
        summit = first_num - second_num
        print('minus')
    elif sign == '*':
        summit = first_num * second_num
        print('times')
    elif sign == '/':
        summit = first_num / second_num
        print('div')
    e.delete(0, END)
    e.insert(0, summit)

def button_plus():
    first = e.get()
    global first_num
    global sign
    first_num = cvtInt(first)
    sign = '+'
    e.delete(0, END)

def button_divide():
    first = e.get()
    global first_num
    global sign
    first_num = cvtInt(first)
    sign = '/'
    e.delete(0, END)

def button_minus():
    first = e.get()
    global first_num
    global sign
    first_num = cvtInt(first)
    sign = '-'
    e.delete(0, END)

def button_times():
    first = e.get()
    global first_num
    global sign
    first_num = cvtInt(first)
    sign = '*'
    e.delete(0, END)

but1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_add(1))
but2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_add(2))
but3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_add(3))
but4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_add(4))
but5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_add(5))
but6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_add(6))
but7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_add(7))
but8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_add(8))
but9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_add(9))
but0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_add(0))
plus = Button(root,text='+',padx=40,pady=20,command=button_plus)
equal = Button(root,text='=',padx=90,pady=20,command=button_equal)
clear = Button(root,text='CLEAR',padx=70,pady=20,command=button_clear)
multiply = Button(root,text='x',padx=40,pady=20,command=button_times)
divide = Button(root,text='/',padx=40,pady=20,command=button_divide)
minus = Button(root,text='-',padx=40,pady=20,command=button_minus)

but1.grid(row=3, column=0)
but2.grid(row=3, column=1)
but3.grid(row=3, column=2)
but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
but7.grid(row=1, column=0)
but8.grid(row=1, column=1)
but9.grid(row=1, column=2)
but0.grid(row=4, column=0)
plus.grid(row=5,column=0)
equal.grid(row=4,column=1, columnspan=2)
clear.grid(row=5,column=1, columnspan=2)
minus.grid(row=6,column=0)
multiply.grid(row=6,column=1)
divide.grid(row=6,column=2)

root.mainloop()