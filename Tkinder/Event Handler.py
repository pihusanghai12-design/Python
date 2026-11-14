from tkinter import *

window= Tk()
window.title("Event Handler")
window.geometry('400x500')

def handle_keypress(event):
    """Print the character assosciated with the key pressed."""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\n The button was clicked")

button= Button(window, text= "Click Me", width= 200, height= 100, bg= "DeepPink2", fg= "white")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()