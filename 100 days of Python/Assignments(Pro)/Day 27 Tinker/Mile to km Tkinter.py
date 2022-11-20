import tkinter

def miles_to_kilo():
    miles = miles_input.get()
    km = float(miles)*1.609
    results_label.config(text=str(km))

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx="20", pady="20")

miles_label = tkinter.Label(text="Enter Miles: ")
miles_label.grid(column=0, row=0)

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

to_kilo_label = tkinter.Label(text="In Kilometers: ")
to_kilo_label.grid(column=0, row=1)

results_label = tkinter.Label(text="0")
results_label.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_kilo)
calculate_button.grid(column=1, row=3)

window.mainloop()
