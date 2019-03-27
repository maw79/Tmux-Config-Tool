import tkinter as tk
# from tkinter import *

window = tk.Tk()

window.title("Tmux Config Tool")

tk.Label(window, text='Bind new horizontal').grid(row=0) 
tk.Label(window, text='Bind new Vertical').grid(row=1) 
e1 = tk.Entry(window) 
e2 = tk.Entry(window) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

button = tk.Button(window, text='Apply', width=10, command=window.destroy).grid(row=3) 

window.mainloop()