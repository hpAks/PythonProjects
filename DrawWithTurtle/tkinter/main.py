import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("GUI interface")
window.minsize(width=500,height=300)




my_label = tkinter.Label(text="I am a Label",font=("Arial", 24,"bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    if len(input.get()) == 0:
        my_label.config(text="I got clicked.")
    else:
        my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1 ,row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

input = Entry()
input.grid(column=3,row=3)
input.config(width=10)



window.mainloop()