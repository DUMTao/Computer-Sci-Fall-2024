# Hello! This is my simple python program that uses tkier for temperature conversion!

import os
import tkinter as tk

window = tk.Tk()
window.title("What's the temperature like?")

def converter():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = int((fahrenheit - 32) * 5.0/9.0)
    
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, str(celsius) + " °C")
    
    except ValueError:
        celsius_entry.delete(0, tk.END)
        f_result.config(text="Please enter a valid number")
    
fahrenheit_var = tk.Label(window, text="Enter temperature in Fahrenheit:")
fahrenheit_var.pack()

fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.pack()

celsius_var = tk.Label(window, text="\n Temperature in Celsius:")
celsius_var.pack()

celsius_entry = tk.Entry(window)
celsius_entry.pack()


button_convert = tk.Button(window, text="Convert", command=converter)
button_convert.pack()

f_result = tk.Label(window, text="")
f_result.pack()




window.mainloop()


