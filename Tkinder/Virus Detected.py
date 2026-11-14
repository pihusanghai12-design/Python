from tkinter import *
from tkinter import messagebox

root= Tk()
root.title("Virus Detected")
root.geometry('500x600')

def msg():
    messagebox.showwarning("Alert!", "Stop, Virus Found" )

button= Button(root, text= "Scan for Virus", command= msg, width= 50, height= 50, bg= "Red3", fg= "White")

button.place(x= 40, y= 80)
root.mainloop()
