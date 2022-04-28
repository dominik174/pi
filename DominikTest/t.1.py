import keyboard
from gpiozero import LED
from time import sleep


def pali_led(x):
    led_nr = 25
    if x == 1:
        led_nr = 25
    elif x == 2:
        led_nr = 17
    elif x == 3:
        led_nr = 13
    elif x == 4:
        led_nr = 20
        pass
    a = LED(led_nr)
    a.on()
    sleep(1)
    a.off()



key_entered = ""
while key_entered != "q":
    key_entered = keyboard.read_key()
    x = parseint(key_entered)
    if x >= 1 and x<=4:
        pali_led(x)
