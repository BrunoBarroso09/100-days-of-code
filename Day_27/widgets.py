from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(500, 300)

#Label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

#Button
def button_clicked():
    user_value = my_input.get()
    my_label.config(text=user_value)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry component
my_input = Entry(width=10)
#Placeholder
my_input.insert(END, "Enter a value")
my_input.pack()

#Text
my_text = Text(height=5, width=35)
#Place cursor in the textbox
my_text.focus()
#Placeholder
my_text.insert(END, "Example of multi-line text entry")
#Get current value in textbox at line 1, character 0
print(my_text.get("1.0", END))
my_text.pack()

#Spinbox
def spinbox_used():
    #Get the current value in spinbox
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=20, width=5, command=spinbox_used)
my_spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)
my_scale = Scale(from_=0, to=200, command=scale_used)
my_scale.pack()

#Checkbutton
def check_used():
    #Print 1 if On button checked, otherwise 0
    print(checked_state.get())
#Variable to hold on to checked state, 0 is off and 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=check_used)
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    #Get current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
cars = ['Opel', 'Honda', 'Nissan', 'Toyota']
for car in cars:
    listbox.insert(cars.index(car), car)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()