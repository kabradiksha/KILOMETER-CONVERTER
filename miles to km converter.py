from tkinter import *

window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.609
    is_equal_kilometer_label.config(text=km)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

is_equal_kilometer_label = Label(text="0")
is_equal_kilometer_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)







window.mainloop()