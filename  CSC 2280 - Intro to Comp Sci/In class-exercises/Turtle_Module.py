import turtle
from math import pi

bawb = turtle.Turtle()


bawb.fd(-330)

'''
def square(t, length):
    for i in range(4):
        bawb.fd(length)
        bawb.lt(90)

    
# Square 1
square(1, 150)
bawb.fd(100)

# Square 2
square(1, 50)
bawb.fd(100)

# Square 3
square(1, 200)
bawb.fd(100)

# Square 4
square(1, 150)
bawb.fd(100)

# Square 5
square(1, 100)
bawb.fd(100)

# Square 6
square(1, 150)
bawb.fd(100)

bawb.fd(150)
'''
def polygon(t, length, n):
    # n = int(360/n)

    for i in range(int(n)):
        bawb.fd(length)
        bawb.lt(360/n)

polygon(1, 50, 7)
bawb.fd(200)


def circle(t, radius):
    circumference = 2 * pi * radius

    bawb = t
    for i in range(1):
        polygon(t, 2, circumference)


circle(1, 60)
bawb.fd(100)


def arc(t, radius, angle):
    length = 
    bawb = t
    angle =  2 * pi * radius * (angle/360)

    for i in range(1):
        polygon(t, radius, angle)

bawb.fd(100)
arc(1, 25, 30)


    

turtle.mainloop()