import turtle
import math
from PIL import Image

l = 44 # length
r = l / math.sqrt(3) # radius
gap = 12 # gap length
angle = math.pi / 2

# setup the window
screen = turtle.Screen()
screen.setup(height=250, width=250)
screen.bgcolor('white')

# Create a turtle object
t = turtle.Turtle()
turtle.colormode(255)
t.pencolor((51, 221, 170))  # Set the pen color
t.pensize(1)  # Set the pen size
t.speed(2)  # Set the drawing speed

t.fillcolor((51, 221, 170))
# draw the flower petal
for i in range(6):
    t.left(60)
    t.penup()
    t.goto(gap * math.cos(angle), gap * math.sin(angle))
    t.pendown()
    t.begin_fill()
    t.forward(l)
    t.circle(r, 240)
    t.forward(l)
    t.end_fill()
    angle = angle - math.pi/3


r = gap/2 + l / math.sqrt(3)

t.penup()
t.pensize(3)
t.goto(math.sqrt(3) / 2 * r, 1.5 * r)

# draw the frame
t.pendown()
for i in range(6):
    t.left(60)
    t.circle(r, 240)
    t.left(120)

turtle.done()