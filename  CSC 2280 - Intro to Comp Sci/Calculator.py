# I'm making a program that allows me to select what formulas I want to calculate and give me the result of them
# Making a GUI as well

# Imports
import math
import tkinter as tk
from tkinter import *

class Application():
# Initialize
    def __init__(self, window):
        window.title("What's your formula today?")
        
        result_button = tk.Button(window, text='Done', command="buttonpressed")
        result_button.pack()
    
    #frame = tk.Frame(window, padding='3 3 12 12')


# Math Database
def formulas():
    def Quatratic(a, b, c):
        result = ( -(b) + math.sqrt((b ** 2) - (4 * a * c)) / (2 * a) )
        return print(f'The answer to your quadratic formula is: {result}')
    









window = Tk()
Application(window)
window.mainloop()
