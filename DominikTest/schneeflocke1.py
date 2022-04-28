import turtle
import random
d = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colors = ["cyan", "purple", "white", "blue"]
numbers = [0,0,0,0]
numbers[0] = 3
numbers[1] = 4
d.penup()
d.forward(90)
d.left(45)
d.pendown()
def branch():
    for i in range(3):
        for i in range(3):
            d.forward(30)
            d.backward(30)
            d.right(45)
        d.left(90)
        d.backward(30)
        d.left(45)
    d.right(90)
    d.forward(90)
for i in range(8):
    branch()
    d.left(45)
#    d.color(random.choice(colors))