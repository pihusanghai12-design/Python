

from tkinter import *

root = Tk()
root.title("ATM PIN Setup Interface")
root.geometry('400x500')

details_frame = Frame(master=root, bg="DeepPink3",
                      height=150, width=360)

name_lbl = Label(details_frame, text="Account Name")
acc_name = Entry(details_frame)

pin_lbl = Label(details_frame, text="Create PIN")
PIN = Entry(details_frame, show="*")


def confirm_pin():
    account_name = acc_name.get()
    pin = PIN.get()

    message_box.delete("1.0", END)

    if account_name == "" or pin == "":
        message_box.insert(
            END,
            "Please fill the ACCOUNT NAME and PIN to proceed."
        )
    else:
        message = ("Hello " + account_name + "!\n"
                   + "Your PIN has been set successfully.\n")
        message_box.insert(END, message)


keypad_frame = Frame(master=root, bg="bisque",
                     relief=SUNKEN, borderwidth=2)

numbers = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1],
           ["Clear", 0, "Enter"]]


for i in range(4):
    keypad_frame.rowconfigure(i, weight=2, minsize=45)

    for j in range(3):
        keypad_frame.columnconfigure(j, weight=2, minsize=55)

        cell = Frame(master=keypad_frame,
                     relief=RAISED, borderwidth=3)

        cell.grid(row=i, column=j, sticky="nsew")

        number_label = Label(
            master=cell,
            text=numbers[i][j],
            bg="coral2",
            fg="white",
            font=("Arial", 15)
        )

        number_label.pack(padx=8, pady=8)


message_box = Text(root, height=4, width=40)

confirm_button = Button(
    root,
    text="Set ATM PIN",
    command=confirm_pin,
    bg="chartreuse4",
    fg="white"
)

details_frame.place(x=20, y=10)

name_lbl.place(x=15, y=25)
acc_name.place(x=155, y=25)

pin_lbl.place(x=15, y=85)
PIN.place(x=155, y=85)

keypad_frame.place(x=115, y=160)

confirm_button.place(x=145, y=375)

message_box.place(x=25, y=420)

root.mainloop()
