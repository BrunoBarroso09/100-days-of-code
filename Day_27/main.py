from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Entry component
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

#Label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(row=0, column=2)

text_label = Label(text="is equal to", font=("Arial", 24, "bold"))
text_label.grid(row=1, column=0)

km_value = Label(text="0", font=("Arial", 24, "bold"))
km_value.grid(row=1, column=1)

km_label = Label(text="KM", font=("Arial", 24, "bold"))
km_label.grid(row=1, column=2)

#Button
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_value.config(text=f'{km}')

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()