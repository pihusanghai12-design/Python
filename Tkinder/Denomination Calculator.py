from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        amount= int(entry.get())
        rate2000= amount // 2000
        amount %= 2000

        rate500 = amount//500
        amount %= 500

        rate100= amount//100
        amount %= 100

        result.config( text= "2000 Notes: " + str(rate2000) +
                       "\n500 Notes: " +str(rate500)+ 
                       "\n100 Notes: "+ str(rate100))

    except:
        messagebox.showerror("Invalid amount", "Please enter a valid amount!")


root= Tk()
root.title("Denomination Calculator")
root.geometry('400x500')

Label(root, text= "Denomination Calculator", font= ("Arial", 20),  fg= "blue", padx = 20, pady= 20 ).pack()
Label(root, text= "Enter Amount", font= ("Arial", 20),  fg= "Black", padx = 20, pady= 20 ).pack()

entry= Entry(root, font= ("Arial", 20))
entry.pack(pady= 5)

Button(root, text= "Calculate", command= calculate, font=("Arial", 20), fg= "White", bg= "Green").pack(pady= 20)
result= Label(root, text= "", font= ("Arial", 20),  fg= "Navy" ).pack(pady= 10)

root.mainloop()



