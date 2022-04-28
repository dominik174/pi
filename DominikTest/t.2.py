import keyboard
from gpiozero import LED
from time import sleep

a = LED(25)
b = LED(17)
c = LED(13)
d = LED(20)

numbers = []

for x in "sasa":
    n = random.randint(1,4)
    numbers.append(n)

for x in numbers:
    