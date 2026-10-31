from tkinter import *

root =Tk()
root.title("Login App")
root.geometry('250x300')

Label(root, text="Name").pack()
name= Entry(root)
name.pack()

Label(root, text="Email").pack()
email= Entry(root)
email.pack()

Label(root, text="Password").pack()
password= Entry(root, show= "*")
password.pack()

textbox = Text(root, height=3, width= 35)
textbox.pack(pady=10)

def create_account():

    textbox.delete("1.0", END)

    textbox.insert(END, f"Hey {name.get()}!\n")

    textbox.insert(END, "Account Created Successfully!")

# Button

Button(root, text="Create Account", command=create_account).pack()

root.mainloop()

