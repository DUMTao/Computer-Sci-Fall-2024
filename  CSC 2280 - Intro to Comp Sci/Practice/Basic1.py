# 1. Write a Python program to print the python version
'''
import os

def PythonVersion():
    os.system('python --version')

PythonVersion()
'''

# 2. Write a Python program to display the current date and time.
'''
import datetime

def Date_Time():
    now = datetime.datetime.now()
    
    print("Current Date and Time: ")
    print(now.strftime("%d/%m/%Y, %H:%M:%S"))
    
Date_Time()
'''

# 3. Write a Python program that calculates the area of a circle based on the radius entered by the user.
''' 
from math import pi

def Area_of_circle():
    radius = int(input("Enter a radius: "))
    area = (pi * radius ** 2)
    return print(area)

Area_of_circle()
'''

# 4. Write a Python program that accepts the user's first and last name 
# and prints them in reverse order with a space between them.
'''
def Full_Name():
    first_name = input("Enter your first name please: ")
    last_name = input("Enter your last name please: ")
    
    print(last_name + ", " + first_name)

Full_Name()
'''

# 5. Write a Python program that accepts a sequence of comma-separated numbers from the user 
# and generates a list and a tuple of those numbers.
'''
def Num_Tuple():
    numbers = input("Enter a sequence of comma-separated numbers: ")
    num_split = numbers.split(',')
    num_tuple = tuple(num_split)
    
    print("Here's your tuple of numbers!")
    print(num_tuple)

def Num_List():
    numbers2 = input("Enter a sequence of comma-separated numbers: ")
    num_split2 = numbers2.split(',')
    num_list = list(num_split2)
    
    print("Here's your list of numbers!")
    print(num_list)

Num_Tuple()
Num_List()
'''

# 6. Write a Python program to display the first and last colors from the following list.
'''
def First_Last_Color():
    color_list = ['Red', 'Green', 'White', 'Black']
    
    print('Here are your first and last colors: ')
    print(color_list[0] + ", " + color_list[-1])

First_Last_Color()
'''

# 7. Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.

def Adder_Multi():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    n3 = int(input("Enter a number: "))
    
    if n1 == n2 and n2 == n3:
        exponent = n1 * 3
        return print(exponent)
    else:
        return print(n1 + n2 + n3)

Adder_Multi()