import tkinter as tk
import pyautogui as pg 
root=tk.Tk()
root.title("Screen Shot GUI")
root.geometry('500x500')
def screenshot():
	screenshot=pg.screenshot()
	screenshot.save("ss.png")
capture=tk.Button(root,text="CAPTURE",command=screenshot)
capture.grid(row=3,column=3)
root.mainloop()