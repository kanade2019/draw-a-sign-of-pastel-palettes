import turtle
import math
from PIL import Image

l = 44
r = l / math.sqrt(3)
gap = 12

screen = turtle.Screen()
screen.setup(height=250, width=250)
screen.bgcolor('white')

t = turtle.Turtle()
turtle.colormode(255)
t.pencolor((51, 221, 170))
t.pensize(1)
t.speed(20)

t.penup()
t.goto(0, gap)
t.left(60)
t.pendown()
t.fillcolor((51, 221, 170))

t.begin_fill()
t.forward(l)
t.circle(r, 240)
t.forward(l)
# t.goto(0, 10)
t.end_fill()

t.penup()
t.goto(gap/2 * math.sqrt(3), gap/2)
t.pendown()
t.begin_fill()
t.left(60)
t.forward(l)
t.circle(r, 240)
t.forward(l)
t.end_fill()

t.penup()
t.goto(gap/2 * math.sqrt(3), -gap/2)
t.pendown()
t.begin_fill()
t.left(60)
t.forward(l)
t.circle(r, 240)
t.forward(l)
t.end_fill()

t.penup()
t.goto(0, -gap)
t.pendown()
t.begin_fill()
t.left(60)
t.forward(l)
t.circle(r, 240)
t.forward(l)
t.end_fill()

t.penup()
t.goto(-gap/2 * math.sqrt(3), -gap/2)
t.pendown()
t.begin_fill()
t.left(60)
t.forward(l)
t.circle(r, 240)
t.forward(l)
t.end_fill()

t.penup()
t.goto(-gap/2 * math.sqrt(3), gap/2)
t.pendown()
t.begin_fill()
t.left(60)
t.forward(l)
t.circle(r, 240)
t.forward(l)
t.end_fill()

r = gap/2 + l / math.sqrt(3)

t.penup()
t.pensize(3)
t.goto(math.sqrt(3) / 2 * r, 1.5 * r)


t.pendown()
for i in range(6):
    t.left(60)
    t.circle(r, 240)
    t.left(120)

turtle.done()