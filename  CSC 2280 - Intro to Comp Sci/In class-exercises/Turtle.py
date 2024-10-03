import turtle
from math import pi

t = turtle.Turtle()

# Initial back up so that the screen isn't taken up
t.fd(-400)

def square(t, length):
    '''
    Write a function called square that takes a parameter named t, which is a turtle. 
    It should use the turtle to draw a square.
    '''
    for i in range(4):
        t.fd(length)
        t.lt(90)

# Squares pt 1 & 2
for i in range(4):
    square(t, 150)
    t.fd(100)


def polygon(t, length, n):
    '''
    Make a copy of square and change the name to polygon. Add another parameter
    named n and modify the body so it draws an n-sided regular polygon.
    '''
    for i in range(int(n)):
        t.fd(length)
        t.lt(360/n)

# Polygon pt 3
for i in range(2):
    polygon(t, 150, 5)
    t.fd(150)


def circle(t, radius):
    '''
    Write a function called circle that takes a turtle, t, and radius, r, as parameters and
    that draws an approximate circle by calling polygon with an appropriate length and
    number of sides. Test your function with a range of values of r.
    '''
    circumference = (2 * pi) * radius
    n = 20
    length = circumference / n
        
    polygon(t, length, n)

circle(t, 100)
t.fd(150)


def arc(t, radius, angle):
    '''
    Make a more general version of circle called arc that takes an additional parameter
    angle, which determines what fraction of a circle to draw. angle is in units of degrees,
    so when angle=360, arc should draw a complete circle.
    '''
    circumference = (2 * pi) * radius
    arc_of_circle = angle / 360
    arc_length = circumference * arc_of_circle
    n = 20
    length = arc_length / n
    degree_turn = angle / n
    
    for i in range(n):
        t.fd(length)
        t.lt(degree_turn)
    

t.fd(200)
arc(t, 130, 90)



turtle.mainloop()