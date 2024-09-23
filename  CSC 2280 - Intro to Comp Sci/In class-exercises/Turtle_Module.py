import turtle
from math import pi

t = turtle.Turtle()


t.fd(-330)

def triange(t, length):
    
    for i in range(3):
        t.fd(length)
        t.lt(120)

for i in range(6):
    triange(t, 50)
    t.lt(60)
    

turtle.mainloop()