import tkinter as tk
from tkinter import *
import os
import numpy as np
from tkinter import messagebox
from tkinter import filedialog
from facedetect import Detections
import cv2 as cv
from PIL import Image, ImageTk


def clear():
    v1.set('')
    global but1, but2, but3
    but1.destroy()
    but2.destroy()
    but3.destroy()


def detect(path, choice):
    img = cv.imread(path)
    h, w, _ = img.shape
    copy = img.copy()
    f = Detections(img)
    if choice == 3:
        f.drawRectFace()
        f.drawCircleeyes(color=(255, 0, 255))
    elif choice == 1:
        f.drawRectFace()
        # f.print()
    elif choice == 2:
        f.drawCircleeyes(color=(255, 0, 255))
    if np.all(img == copy):
        messagebox.showinfo("Detection Error", "No Faces/Eyes Detected")
        return

    root1 = Toplevel()
    # canvas = Canvas(root1, width=w, height=h)

    root1.title("Detected Image")
    root1.iconbitmap(os.path.abspath('image.ico'))
    root1.resizable(0, 0)
    path = path.split('/')[-1]
    cv.imwrite(path, img)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    panel = tk.Label(root1, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    root1.mainloop()


def both(f):
    f.drawRectFace()
    f.drawCircleeyes()


def camera():
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        _, frame = cap.read()
        f = Detections(frame)

        f.drawRectFace()
        f.drawCircleeyes(scale=1.2, color=(0, 255, 0))
        f.showVideoFrame(cap)


def browse():
    file = filedialog.askopenfile(filetypes=[('Image Files', '*.jpg'), ('PNG files', '*.png')])
    if file is not None:
        Label(root, textvariable=v1, font=('arial', 10, 'bold'), bd=6, justify=tk.CENTER).grid(row=2, column=1, pady=10,
                                                                                               columnspan=10,
                                                                                               sticky=N)
        v1.set(file.name.split('/')[-1])
        global but1, but2, but3
        but1 = Button(root, text='Detect Faces', fg='white', bg='green', height=1, width=20,
                      command=lambda: detect(file.name, 1))
        but1.grid(row=3, column=1, pady=10, columnspan=10,
                  sticky=N)
        but2 = Button(root, text='Detect Eyes', fg='white', bg='green', height=1, width=20,
                      command=lambda: detect(file.name, 2))
        but2.grid(row=4, column=1, pady=10, columnspan=10,
                  sticky=N)
        but3 = Button(root, text='Detect Face and Eyes', fg='white', bg='green', height=1, width=20,
                      command=lambda: detect(file.name, 3))
        but3.grid(row=5, column=1, pady=10, columnspan=10,
                  sticky=N)


but1, but2, but3 = "", "", ""
root = tk.Tk()
v1 = StringVar()
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('+%d+%d' % (x, y))
root.iconbitmap(os.path.abspath('faceico.ico'))
root.title("Face Detection")
root.resizable(0, 0)

Button(root, text='Browse', fg='white', bg='blue', height=1, width=20,
       command=lambda: browse()).grid(row=1, column=1, pady=10,
                                      sticky=W)
Button(root, text='Clear', fg='white', bg='red', height=1, width=20,
       command=lambda: clear()).grid(row=1, column=2, pady=10, columnspan=10,
                                     sticky=W)
Button(root, text='Live Detection', fg='white', bg='green', height=1, width=20,
       command=lambda: camera()).grid(row=10, column=1, pady=10, padx=70, columnspan=30,
                                      sticky=NW)
root.mainloop()
