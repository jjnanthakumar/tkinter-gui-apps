import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

turns = 0
guessed = []


def check_number(g, mynum, tk_turns, tk_guess, name, root1):
    global guessed, turns
    if g in guessed:
        return
    turns += 1
    guessed.append(g)
    if g == mynum:
        v = messagebox.askyesno(title="Guess Result",
                                message="Congragulations {}! You won\nWant to play again?".format(name.capitalize()))
        if v:
            turns = 0
            guessed = []
            root1.destroy()
            guess()
        else:
            messagebox.showinfo(title="Greeting", message="Thanks for playing {} :)".format(name.capitalize()))
            root1.destroy()
    if g < mynum:
        Label(root1, text=f"Wrong Guess :( {str(g)} is less than the number", justify=tk.CENTER,
              fg="red").grid(row=3, column=0,
                             columnspan=30,
                             pady=10,
                             sticky=N)
    else:
        Label(root1, text=f"Wrong Guess :( {str(g)} is greater than the number", justify=tk.CENTER,
              fg="red").grid(row=3, column=0,
                             columnspan=30,
                             pady=10,
                             sticky=N)
    tk_turns.set("Remaining Turns : {}".format(6 - turns))
    tk_guess.set("Already Guessed : {}".format(' '.join(map(str, guessed))))

    if 6 - turns == 0:
        f = messagebox.askretrycancel(title="Guess Result",
                                      message="Better Luck Next time {}, You Lose :(\n The Number is {}".format(
                                          name.capitalize(), mynum))
        if f:
            turns = 0
            guessed = []
            root1.destroy()
            guess()
        else:
            messagebox.showinfo(title="Greeting", message="Thanks for playing {} :)".format(name.capitalize()))
            root1.destroy()


def start(root, v1):
    hiddennum = random.randint(1, 20)
    name = v1.get().split()[0]
    if not name.isalpha():
        messagebox.showerror(title="Error",
                             message="Name must be a set of characters :(")
        return
    root.destroy()
    root1 = Tk()
    w = root1.winfo_reqwidth()
    h = root1.winfo_reqheight()
    ws = root1.winfo_screenwidth()
    hs = root1.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root1.geometry('+%d+%d' % (x, y))
    root1.iconbitmap(os.path.abspath('guess.ico'))

    root1.title("Hangman")
    root1.resizable(0, 0)
    txt = "Hello {}, Welcome to Guess a Number Game :)".format(name.capitalize())
    Label(root1, text=txt, font=('arial', 10, 'bold'), justify=tk.CENTER, padx=10, fg="blue").grid(row=1, column=0,
                                                                                                   columnspan=30,
                                                                                                   sticky=W, pady=10,
                                                                                                   padx=10)
    Label(root1, text="Guess a number between 1 to 20 :)", justify=tk.CENTER, padx=10, fg="green").grid(row=2, column=1,
                                                                                                        columnspan=30,
                                                                                                        pady=10,
                                                                                                        sticky=W)
    c, r = 0, 6
    for i in range(1, 21):
        Button(root1, text=i, fg='blue', bg='white', height=3, width=5,
               command=lambda g=i: check_number(g, hiddennum, tk_turns, tk_guess,
                                                name,
                                                root1)).grid(
            row=r,
            column=c,
            sticky=N,
            padx=10)
        if i >= 4 and c == 4:
            c = 0
            r += 1
            continue
        c += 1

    tk_turns = StringVar()
    tk_guess = StringVar()

    tk_turns.set("Remaining Turns : {}".format(6))
    Label(root1, textvariable=tk_turns, font=('arial', 10, 'bold'), bd=10, justify=tk.CENTER, padx=10).grid(row=4,
                                                                                                            column=1,
                                                                                                            columnspan=30,
                                                                                                            sticky=W)
    tk_guess.set("Already Guessed : {}".format('None'))
    Label(root1, textvariable=tk_guess, font=('arial', 10, 'bold'), bd=10, justify=tk.CENTER, padx=10).grid(row=5,
                                                                                                            column=1,
                                                                                                            columnspan=30,
                                                                                                            sticky=W)


def guess():
    root = tk.Tk()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('+%d+%d' % (x, y))
    root.iconbitmap(os.path.abspath('guess.ico'))
    root.title("Guessing Game")
    root.resizable(0, 0)
    v1 = StringVar()
    v1.set('')
    Label(root, text="Enter Your Name: ", justify=tk.LEFT, padx=10).grid(row=1, column=0, sticky=W)
    Entry(root, textvariable=v1, fg='blue', width=30, justify=tk.CENTER).grid(row=1, column=1, sticky=W, pady=2,
                                                                              padx=10,
                                                                              columnspan=10)

    Button(root, text='start', fg='white', bg='blue', height=1, width=3,
           command=lambda: start(root, v1)).grid(row=2, column=4, pady=10,
                                                 sticky=W)

    root.mainloop()


guess()
