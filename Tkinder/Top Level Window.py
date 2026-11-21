from tkinter import *
root= Tk()

def open_window():
    top= TopLevel()
    top.title("Top Title Window")
    top.gemetry('200x200')

    Label(top, text= "Hello World", font= ("Arial", 20),  fg= "blue", padx = 20, pady= 20 ).pack()

Button= Button(root, text= "Open Window", command= open_window, font=("Arial", 20), fg= "White", bg= "Green").pack(pady= 20)
root.mainloop()    