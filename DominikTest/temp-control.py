import RPi.GPIO as GPIO
import time
import os

MotorPin_A  = 11
MotorPin_B  = 12

# def motorStop():
# 	GPIO.output(MotorPin_A, GPIO.HIGH)
# 	GPIO.output(MotorPin_B, GPIO.HIGH)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(MotorPin_A, GPIO.OUT)
	GPIO.setup(MotorPin_B, GPIO.OUT)
	motor(0,0)

def motor(status, direction):
	if status == 1:  # run
		if direction == 1:
			GPIO.output(MotorPin_A, GPIO.HIGH)
			GPIO.output(MotorPin_B, GPIO.LOW)
		else:
			GPIO.output(MotorPin_A, GPIO.LOW)
			GPIO.output(MotorPin_B, GPIO.HIGH)
	else:  # stop
		GPIO.output(MotorPin_A, GPIO.HIGH)
		GPIO.output(MotorPin_B, GPIO.HIGH)

def loop1():
	while True:
		motor(1, 1)
		time.sleep(5000)
		motor(0, 1)
		time.sleep(5000)
		motor(1, 0)
		time.sleep(5000)

def destroyMotor():
	motor(0,0)
	GPIO.cleanup()             # Release resource

def readSensor(id):
	tfile = open("/sys/bus/w1/devices/"+id+"/w1_slave")
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	global temperature
	temperature = temperature / 1000
	print("Sensor: " + id  + " - Current temperature : %0.3f C" % temperature)

# Reads temperature from all sensors found in /sys/bus/w1/devices/
# starting with "28-...
def readSensors():
	count = 0
	sensor = ""
	for file in os.listdir("/sys/bus/w1/devices/"):
		if (file.startswith("28-")):
			readSensor(file)
			count+=1
	if (count == 0):
		print("No sensor found! Check connection")

# read temperature every second for all connected sensors
def loop():
	while True:
		readSensors()
		time.sleep(1)
		if temperature >= value:
			try:
				motor(1,1)
			except KeyboardInterrupt:
				totalStop()
		if temperature < value:
			motor(0,0)

# Nothing to cleanup
def destroyTempCalculator():
	pass

def totalStop():
	destroyTempCalculator()
	destroyMotor()

def start():
	setup()
	loop()

# Main starts here
if __name__ == "__main__":
	print("Na koliko stupnjeva da ohladim sobu?")
	value = float(input())
	try:
		start()
	except KeyboardInterrupt:
		totalStop()
		