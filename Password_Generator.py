import random
import tkinter
from tkinter import *
from tkinter.ttk import *
import pyperclip


def low():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    pwd = ""

    if var.get() == 1:
        for i in range(0, length):
            pwd = pwd + random.choice(lower)
        return pwd
    elif var.get() == 0:
        for i in range(0, length):
            pwd = pwd + random.choice(upper)
        return pwd
    elif var.get() == 2:
        for i in range(0, length):
            pwd = pwd + random.choice(digits)
        return pwd
    else:
        print("Choose an option")


def generate():
    pwd1 = low()
    entry.insert(10, pwd1)


def copy1():
    random_pwd = entry.get()
    pyperclip.copy(random_pwd)


root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Password Generator")

Random_pwd = Label(root, text="pwd")
Random_pwd.grid(row=4)
entry = Entry(root)
entry.grid(row=4, column=1)

c_label = Label(root, text="Length")
c_label.grid(row=1)

generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=3, column=1)
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=4, column=2)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=3, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=4, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=2)
radio_strong.grid(row=1, column=5, sticky='E')
combo = Combobox(root, textvariable=var1)

combo['values'] = (
    8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)


root.mainloop()