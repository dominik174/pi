import turtle
inkrement = int(input("Inkrement?"))
d = turtle.Turtle()
d.right(45)
def zunahme(x):
 #  x = 10
    while x <= 100:
            x = x+inkrement
            d.forward(x)
            d.left(90)
            d.forward(x+inkrement)
def abnahme(x):
#   x = 100
    while x >= 0:
            x = x-inkrement
            d.forward(abs(x))
            d.right(90)
            d.forward(abs(x-inkrement))
for i in range(1):
    zunahme(10)
    d.forward(150)
    abnahme(100)