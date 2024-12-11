# I'm making a program that allows me to select what formulas I want to calculate and give me the result of them
# Making a GUI as well

# Imports
import math
import tkinter as ttk
from tkinter import *
from formulas import *

class Application():
# Beginning functions to display the window
    
    def create_frame(window):
        frame = Frame(window)
        
        #Create grid for input
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=3)
        
        #Asks for input for course name
        ttk.Label(frame, text="What's the course name?").grid(column=0, row=0, sticky=ttk.W)
        course_name = ttk.Entry(frame, width=31)
        course_name.focus()
        course_name.grid(column=1, row=0, sticky=ttk.W)
        
        # If checked, it will round to the nearest tens
        round_result = ttk.StringVar()
        round_result_check = ttk.Checkbutton(
            frame, 
            text="Round to tens", 
            variable=round_result,
            command=lambda: round_result.set(round_result.get())
        )
        round_result_check.grid(column=0, row=1, sticky=ttk.W)
        
        
        
    def main_window():
        root = ttk.Tk()
        root.title("What will you have today sir?")
        
        root.resizable(0,0)
        
        # For windows
        try:
            root.attributes('-toolwindow', True)
        except TclError:
            print('Womp womp, wrong OS buddy')
        
        # Layout for the root window
        root.columnconfigure(0, weight=4)
        root.columnconfigure(1, weight=1)
        









window = ttk.Tk()
window.mainloop()
