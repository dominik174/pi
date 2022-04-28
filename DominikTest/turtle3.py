import turtle
import random
d = turtle.Turtle()
turtle.Screen().bgcolor("grey")
for i in range(10):
    colours = ["cyan", "purple", "white", "blue"]
    d.color(random.choice(colours))
    for i in range(2):
        d.forward(100)
        d.right(60)
        d.forward(100)
        d.right(120)
    d.right(36)