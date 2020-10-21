import Tkinter as tk
from Tkinter import *
from math import sin, cos, tan


def calc(name):
    v.set(v.get() + name)


def clear():
    v.set('')


def operations(name):
    a = str(v.get())
    try:
        oper = {'+': a + '+', '-': a + '-', '*': a + '*', '/': a + '/', '%': a + '%', '=': eval(a),
                'sin': 'sin(' + a + ')', 'cos': 'cos(' + a + ')', 'tan': 'tan(' + a + ')', 'pow': a + '**',
                '.': a + '.', '0': a + '0', '00': a + '00'}

        v.set(oper[name])

    except:
        print "Invalid Operation"


root = tk.Tk()
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('+%d+%d' % (x, y))
root.iconbitmap('calc.ico')
root.title("Calculator")
root.resizable(0, 0)
c = 0
r = 1
but_obj = []
for i in range(1, 10):
    Button(root, text=str(i), fg='blue', bg='white', height=4, width=6,
           command=lambda name=str(i): calc(name)).grid(row=r,
                                                        column=c,
                                                        sticky=W,
                                                        padx=0)
    if i >= 3 and c == 2:
        c = 0
        r += 1
        continue
    c += 1
v = StringVar()
Entry(root, textvariable=v, font=('Arial', 10, 'bold'), fg='red', width=44).grid(row=0, column=0, ipady=7, sticky=W,
                                                                                 pady=10, columnspan=30)
Button(root, text='+', fg='blue', bg='white', height=4, width=6,
       command=lambda name='+': operations(name)).grid(row=2,
                                                       column=3,
                                                       sticky=W)

Button(root, text='=', fg='blue', bg='white', height=4, width=6,
       command=lambda name='=': operations(name)).grid(row=3,
                                                       column=3,
                                                       sticky=W)
Button(root, text='C', fg='blue', bg='white', height=4, width=6,
       command=lambda: clear()).grid(row=1,
                                     column=3,
                                     sticky=W)

Button(root, text='*', fg='blue', bg='white', height=4, width=6,
       command=lambda name='*': operations(name)).grid(row=1,
                                                       column=4,
                                                       sticky=W)
Button(root, text='-', fg='blue', bg='white', height=4, width=6,
       command=lambda name='-': operations(name)).grid(row=2,
                                                       column=4,
                                                       sticky=W)
Button(root, text='/', fg='blue', bg='white', height=4, width=6,
       command=lambda name='/': operations(name)).grid(row=3,
                                                       column=4,
                                                       sticky=W)
Button(root, text='%', fg='blue', bg='white', height=4, width=6,
       command=lambda name='%': operations(name)).grid(row=1,
                                                       column=5,
                                                       sticky=W)
Button(root, text='sin', fg='blue', bg='white', height=4, width=6,
       command=lambda name='sin': operations(name)).grid(row=2,
                                                         column=5,
                                                         sticky=W)
Button(root, text='cos', fg='blue', bg='white', height=4, width=6,
       command=lambda name='cos': operations(name)).grid(row=3,
                                                         column=5,
                                                         sticky=W)
Button(root, text='pow', fg='blue', bg='white', height=4, width=6,
       command=lambda name='pow': operations(name)).grid(row=4,
                                                         column=3,
                                                         sticky=W)
Button(root, text='.', fg='blue', bg='white', height=4, width=6,
       command=lambda name='.': operations(name)).grid(row=4,
                                                       column=2,
                                                       sticky=W)
Button(root, text='00', fg='blue', bg='white', height=4, width=6,
       command=lambda name='00': calc(name)).grid(row=4,
                                                  column=0,
                                                  sticky=W)
Button(root, text='0', fg='blue', bg='white', height=4, width=6,
       command=lambda name='0': calc(name)).grid(row=4,
                                                 column=1,
                                                 sticky=W)
Button(root, text='tan', fg='blue', bg='white', height=4, width=6,
       command=lambda name='tan': operations(name)).grid(row=4,
                                                         column=4,
                                                         sticky=W)
root.mainloop()
