import keyboard
import random
from gpiozero import LED
from time import sleep

# dictionary
led_pins = {
    1:25,
    2:17,
    3:13,
    4:20
}

# Pali led
def pali_led(x):
    led_nr = led_pins[x]
    a = LED(led_nr)
    a.on()
    sleep(1)
    a.off()

numbers = []

# generiranje radnom brojeva
def random_br():
    for x in "sasa":
        n = random.randint(1,4)
        numbers.append(n)
    for x in numbers:
        pali_led(x)

random_br()
print(numbers)
# string - array
print("Upisite kako su se palile lampice")
brojevi = input()
brojevi_arr = []
for x in brojevi:
    brojevi_arr.append(int(x))

while numbers == brojevi_arr:
    random_br()
    print("Upisite kako su se palile lampice")
    brojevi = input()
    brojevi_arr = []
    for x in brojevi:
        brojevi_arr.append(int(x))

if numbers != brojevi_arr:
    print("Krivo ste brojeve upisali! Game over!")
