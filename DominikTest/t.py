import keyboard
from gpiozero import LED
from time import sleep

a = LED(25)
b = LED(17)
c = LED(13)
d = LED(20)

key_entered = ""
while key_entered != "q":
    key_entered = keyboard.read_key()
    if key_entered == "1":
        a.on()
        sleep(1)
        a.off()
    if key_entered == "2":
        b.on()
        sleep(1)
        b.off()
    if key_entered == "3":
        c.on()
        sleep(1)
        c.off()
    if key_entered == "4":
        d.on()
        sleep(1)
        d.off()
