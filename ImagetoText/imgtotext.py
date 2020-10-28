import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pytesseract
from tkinter import filedialog
import pyautogui
import time
import random, os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pywinauto import Application


# app = Application(backend="win32").start('notepad.exe')
# # app.UntitledNotepad.minimize()
# app.UntitledNotepad.Edit.set_text('some text\nsecond line')
def savetext(data, root1):
    data = data.split('\n')
    fname = f'convertedfile{random.randint(1, 1000)}.txt'
    with open(fname, 'a+') as f:
        for dat in data:
            f.write(dat.strip() + '\n')
    path = os.path.abspath(fname)
    m = messagebox.showinfo("File Creation",
                            f"TextFile Created Successfully :)\nFile Name : {fname}\nFile Path : {path}")
    if m:
        root1.destroy()


def saveauto(data):
    data = data.split('\n')
    pyautogui.press('winleft')
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    time.sleep(4)
    # print(pyautogui.position())
    # 645,166

    pyautogui.click(645, 166)

    # pyautogui.click()
    for dat in data:
        dat = dat.replace('  ', '').replace('', '').replace('   ', '')
        pyautogui.typewrite(dat)
        pyautogui.press('enter')
    # print(data)


def imgtotext(path):
    data = pytesseract.image_to_string(path)
    import re
    if not bool(re.match(r'[0-9a-zA-Z]+',data)):
        messagebox.showerror("Conversion Error","No Text Found")
        return
    root1 = Tk()
    root1.title("Converted Text")
    root1.iconbitmap(r'C:\Users\Nanthakumar J J\Desktop\projects\Tkinter GUI\ImagetoText\favicon.ico')
    Label(root1, text=data, font=('arial', 10, 'bold'), bd=6, justify=tk.CENTER).grid(row=2, column=0, pady=10,
                                                                                      columnspan=10,
                                                                                      sticky=N)
    Button(root1, text='Auto type in notepad', fg='white', bg='green', height=1, width=20,
           command=lambda: saveauto(data)).grid(row=1, column=3, pady=10,
                                                sticky=NE)
    Button(root1, text='Save as text file', fg='white', bg='green', height=1, width=20,
           command=lambda: savetext(data, root1)).grid(row=1, column=4, pady=10,
                                                       sticky=NE)
    root1.mainloop()


def clear():
    global but1
    v1.set('')
    but1.destroy()


def browse():
    file = filedialog.askopenfile(filetypes=[('Image Files', '*.jpg'), ('PNG files', '*.png')])
    if file is not None:
        Label(root, textvariable=v1, font=('arial', 10, 'bold'), bd=6, justify=tk.CENTER).grid(row=2, column=1, pady=10,
                                                                                               columnspan=10,
                                                                                               sticky=N)
        v1.set(file.name.split('/')[-1])
        global but1, but2, but3
        but1 = Button(root, text='Convert to Text', fg='white', bg='green', height=1, width=20,
                      command=lambda: imgtotext(file.name))
        but1.grid(row=3, column=1, pady=10, columnspan=10,
                  sticky=N)


but1 = ""
root = tk.Tk()
v1 = StringVar()
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('+%d+%d' % (x, y))
root.iconbitmap(r'C:\Users\Nanthakumar J J\Desktop\projects\Tkinter GUI\ImagetoText\conve.ico')
root.title("Conversion")
root.resizable(0, 0)

Button(root, text='Browse', fg='white', bg='blue', height=1, width=20,
       command=lambda: browse()).grid(row=1, column=1, pady=10,
                                      sticky=W)
Button(root, text='Clear', fg='white', bg='red', height=1, width=20,
       command=lambda: clear()).grid(row=1, column=2, pady=10, columnspan=10,
                                     sticky=W)

root.mainloop()
