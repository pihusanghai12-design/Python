from tkinter import *
from datetime import date

root = Tk()
root.title("Workshop Participant Greeting")
root.geometry('600x700')

lbl= Label(text= "Workshop Welcome desk", fg= "white", bg= "Navyblue", height= 1, width= 300)

name_lbl= Label(text= "Participant Name: ", bg= "Yellow")

name_entry= Entry()

def display_welcome():
    name= name_entry.get()

    text_box.delete("1.0", END)

    greeting= "Hello," +name+ "!\n"
    message= "Welcome to the Workshop. \n"
    workshop_date= "Today's date is: " + str(date.today())

    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_date)

text_box= Text(height= 4, width= 50)

button= Button(text= "Check-In", command= display_welcome, height=3, bg= "IndianRed", fg= "White")

lbl.pack()
name_lbl.pack()
name_entry.pack()
button.pack()
text_box.pack()

root.mainloop()
