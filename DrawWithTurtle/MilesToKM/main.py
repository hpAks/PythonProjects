from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
window.title("Mile to KM Converter")

def calculate_km():
    km = float(input.get()) *1.609
    ans_label.config(text=f"{km}")

input = Entry()
input.grid(column=1, row=0)
input.config(width=10)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_to_label = Label()
is_equal_to_label.config(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)

ans_label = Label()
ans_label.config(text="0")
ans_label.grid(column=1, row=1)

button = Button(text="Calculate" ,command=calculate_km)
button.config(width=10)
button.grid(column=1, row=2)






window.mainloop()