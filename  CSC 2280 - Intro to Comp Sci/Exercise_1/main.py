import os
import tkinter as tk

window = tk.Tk()
window.title("What's the temperature like?")

fahrenheit_var = tk.StringVar()

def submit():
    fahrenheit = float(fahrenheit_var.get())
    celsius = (fahrenheit - 32) * 5.0/9.0
    
btn_submit = tk.Label(text='Enter temperature in Fahrenheit', font=('Arial', 12), width=15, height=5)
enter_f = tk.Entry(textvariable=fahrenheit_var)
btn_submit.pack()
enter_f.pack()




window.mainloop()


