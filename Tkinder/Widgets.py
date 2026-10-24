from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with Widgets.")
root.geometry('600x700')

lb1= Label(text= "Hey There!", fg= "white", bg= "Blue", height= 3, width= 300)

name_lb1= Label(text= "Full Name: ", bg= "Red")

name_entry= Entry()

def display():
    name= name_entry.get()

    global Message
    message= "Welcome to the application. \n Today's date is: "
    greet= "Hello",  name, "\n"

    textbox.insert (END, greet)
    textbox.insert (END, message)
    textbox.insert (END, date.today())

textbox=  Text(height= 5)   

btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

# Organize all the widgets in the window

lb1.pack()

name_lb1.pack()

name_entry.pack()

btn.pack()

textbox.pack()

# Start the GUI event loop

root.mainloop()
    

