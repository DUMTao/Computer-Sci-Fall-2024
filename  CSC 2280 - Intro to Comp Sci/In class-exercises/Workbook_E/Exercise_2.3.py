from math import pi
"""
def area_of_circle(radius):
    formula = float((pi) * (radius ** 2))
    print(f'The area of the circle with a radius of {radius} is {formula: .2f}')

area_of_circle(5)
area_of_circle(10)
area_of_circle(15)
area_of_circle(20)
area_of_circle(25)
"""

def area_of_rec(width, height):
    formula = width * height
    print(f'The area of the rectangle with a width of {width} and a height of {height} is {formula}')

width = float(input('Enter a width: '))
height = float(input('Enter a height: '))
area_of_rec(width, height)

