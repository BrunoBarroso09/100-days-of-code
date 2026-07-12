from tkinter import *

window = Tk()
window.title("Grid Challenge")
window.minsize(500, 300)
window.config(padx=20, pady=20)

my_label = Label(text="Label")
my_label.grid(row=0, column=0)

my_button = Button(text="Click Me")
my_button.grid(row=1, column=1)

new_button = Button(text="Click")
new_button.grid(row=0, column=2)

my_entry = Entry(width=10)
my_entry.grid(row=2, column=3)

window.mainloop()