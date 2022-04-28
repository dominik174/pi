from gpiozero import LED
from time import sleep

a = LED(25)
b = LED(17)
c = LED(13)
d = LED(20)

while True:
    a.on()
    sleep(1)
    a.off()
    sleep(1)