import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
win=tk.Tk()
win.title("Random Number Generator")
def play():
    random_number=random.randint(1,6)
    number.config(text=f"Number is :{random_number}")
    if random_number==6:
        showinfo("Congratulations","You Won!!")
number=ttk.Label(win,text="")
number.pack(pady=10)
play=ttk.Button(win,text="Play",command=play)
play.pack(padx=50)
win.mainloop()