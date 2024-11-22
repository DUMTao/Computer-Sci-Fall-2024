import os
import tkinter as tk

window = tk.Tk()
window.title("What's the temperature like?")

def converter():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5.0/9.0
    
        result.config(text=f"{fahrenheit} °F is equal to {celsius:.2f} °C")
    
    except ValueError:
        result.config(text="Please enter a valid number")
    
fahrenheit_var = tk.Label(window, text="Enter temperature in Fahrenheit:")
fahrenheit_var.pack()

fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.pack()

button_convert = tk.Button(window, text="Convert", command=converter)
button_convert.pack()

result = tk.Label(window, text="")
result.pack()




window.mainloop()


