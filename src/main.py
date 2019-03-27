import tkinter as tk
from tkinter import messagebox
import os
from os import path
# from tkinter import *

window = tk.Tk()

window.title("Tmux Config Tool")

tk.Label(window, text='Bind new horizontal').grid(row=0)
tk.Label(window, text='Bind new Vertical').grid(row=1)
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def apply():
    if(path.exists('~/.tmux.conf')):
        f = open("~/.tmux.conf", 'w')
    else:
        messagebox.showinfo("Error", ".tmux.conf does not exists in your home directory")

button = tk.Button(window, text='Apply', width=10, command=apply).grid(row=3)

window.mainloop()