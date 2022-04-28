import turtle
d = turtle.Turtle()
d.right(45)
def branch():
    x = 10
    for i in range(1):
        while x <= 100:
            x = x+10
            d.forward(x)
            d.left(90)
            d.forward(x+10)
        d.forward(150)
        while x != 0:
            x = x-10
            d.forward(x)
            d.right(90)
            d.forward(x-10)
        d.left(90)
        d.forward(10)
for i in range(1):
    branch()