import numpy as np
import cv2 as cv
import random
import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def randomword(name, serviceurl='https://api.datamuse.com/words?'):
    char = random.choice(list(name))
    serviceurl += 'sp=' + char + '*' + '&max=500'

    r = requests.get(serviceurl)
    try:
        data = r.content
        data = json.loads(data)
    except:
        raise ValueError("Datamuse Server Problem! Hang on For a minute :)")
    return random.choice([ele['word'] for ele in data if len(ele['word']) > 5])


turns = 0

guessed = ""


def check_words(find, hidden_word, hashed, hashed_text, tk_turns, tk_guess, name, root1):
    global turns, guessed
    if find in guessed:
        return
    # if turns == 0:
    #     print(' '.join(hashed))

    guessed += find
    if find not in hidden_word:
        turns += 1
    for i, j in enumerate(hidden_word):
        if j == find:
            hashed[i] = j
    hashed = ' '.join(hashed)
    hashed_text.set(hashed)
    tk_turns.set("Remaining Turns : {}".format(10 - turns))
    tk_guess.set("Already Guessed : {}".format(guessed))
    if '_' not in hashed:
        v = messagebox.askyesno(title="Hangman Result",
                                message="Congragulations {}! You won\nWant to play again?".format(name.capitalize()))
        if v:
            turns = 0
            guessed = ''
            root1.destroy()
            hangmangame()
        else:
            messagebox.showinfo(title="Greeting", message="Thanks for playing {} :)".format(name.capitalize()))
            root1.destroy()
    if 10 - turns == 0:
        f = messagebox.askretrycancel(title="Hangman Result",
                                      message="Better Luck Next time {}, You Lose :(\n The word is {}".format(
                                          name.capitalize(), hidden_word))
        if f:
            turns = 0
            guessed = ''
            root1.destroy()
            hangmangame()
        else:
            messagebox.showinfo(title="Greeting", message="Thanks for playing {} :)".format(name.capitalize()))
            root1.destroy()


def start(root, v1):
    name = v1.get()
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
    root1.iconbitmap(os.path.abspath('hang.ico'))

    root1.title("Hangman")
    root1.resizable(0, 0)
    txt = "Hello {}, Welcome to Hangman Game!!".format(name.capitalize())
    Label(root1, text=txt, font=('arial', 9, 'bold'), justify=tk.CENTER, padx=10, fg="blue").grid(row=1, column=0,
                                                                                                  columnspan=30,
                                                                                                  sticky=W, pady=10,
                                                                                                  padx=10)
    hidden_word = randomword(v1.get()).replace(' ', '')
    Label(root1, text="Start Guessing....", justify=tk.CENTER, padx=10, fg="red").grid(row=2, column=2, columnspan=30,
                                                                                       pady=10,
                                                                                       sticky=W)
    c, r = 0, 6
    for i in range(97, 123):
        Button(root1, text=chr(i), fg='blue', bg='white', height=3, width=5,
               command=lambda guess=chr(i): check_words(guess, hidden_word, hashed, hashed_text, tk_turns, tk_guess,
                                                        name,
                                                        root1)).grid(
            row=r,
            column=c,
            sticky=W,
            padx=0)
        if i >= 6 and c == 6:
            c = 0
            r += 1
            continue
        c += 1

    hashed = list("_" * len(hidden_word))

    hashed_text = StringVar()
    tk_turns = StringVar()
    tk_guess = StringVar()
    hashed_text.set(' '.join(hashed))
    Label(root1, textvariable=hashed_text, font=('arial', 16, 'bold'), bd=16, justify=tk.CENTER, padx=10).grid(row=3,
                                                                                                               column=1,
                                                                                                               columnspan=30,
                                                                                                               sticky=W)
    tk_turns.set("Remaining Turns : {}".format(10))
    Label(root1, textvariable=tk_turns, font=('arial', 10, 'bold'), bd=10, justify=tk.CENTER, padx=10).grid(row=4,
                                                                                                            column=1,
                                                                                                            columnspan=30,
                                                                                                            sticky=W)
    tk_guess.set("Already Guessed : {}".format('None'))
    Label(root1, textvariable=tk_guess, font=('arial', 10, 'bold'), bd=10, justify=tk.CENTER, padx=10).grid(row=5,
                                                                                                            column=1,
                                                                                                            columnspan=30,
                                                                                                            sticky=W)


# def doSomethingOnExit(root):
#     if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
#         root.withdraw()
#     else:
#         hangmangame()
import os


def hangmangame():
    root = tk.Tk()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('+%d+%d' % (x, y))
    root.iconbitmap(os.path.abspath('hang.ico'))
    root.title("Hangman Game")
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


hangmangame()
