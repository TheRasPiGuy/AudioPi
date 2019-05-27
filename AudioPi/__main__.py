import RPi.GPIO as gpio
import subprocess
import shlex
import datetime
import time
from threading import Thread

def setup():
	gpio.setmode(gpio.BOARD)
	gpio.setup(29, gpio.OUT)
	gpio.setup(31, gpio.OUT)
	gpio.setup(33, gpio.OUT)
	gpio.setup(37, gpio.IN, pull_up_down=gpio.PUD_UP)

recording = False

global p

prev_inp = 1

def setled(pin, value):
	gpio.output(pin, value)

def ledrecording():
	while True:
		global recording
		if recording:
			setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.HIGH))
			time.sleep(0.125)
			setled((29, 31, 33), (gpio.LOW, gpio.LOW, gpio.LOW))
			time.sleep(1.5)

def ledidle():
	while True:
		global recording
		if not recording:
			setled((29, 31, 33), (gpio.LOW, gpio.LOW, gpio.HIGH))
			time.sleep(0.8)
			setled((29, 31, 33), (gpio.LOW, gpio.LOW, gpio.LOW))
			time.sleep(0.8)

def ledstartup():
	setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.HIGH, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.HIGH, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.HIGH, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.LOW, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.HIGH, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.HIGH, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.HIGH, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.LOW, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.HIGH, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.HIGH, gpio.LOW))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.HIGH, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.LOW, gpio.LOW, gpio.HIGH))
	time.sleep(0.08)
	setled((29, 31, 33), (gpio.HIGH, gpio.LOW, gpio.HIGH))
	time.sleep(0.08)

def BtnCheck(pin):
	global prev_inp
	inp = gpio.input(pin)
	if ((not prev_inp) and inp):
		toggle()
	prev_inp = inp
	time.sleep(0.05) 

def toggle():
	global recording
	recording = not recording
	global p
	if recording:
		print("Recording...")
		currentDT = datetime.datetime.now()
		filename = '/home/pi/Recordings/Recording_' + currentDT.strftime('%m-%d-%Y_%H:%M:%S') + '.wav'
		command = 'arecord --device=hw:1,0 --format S16_LE --rate 48000 -c1 ' + filename
		p = subprocess.Popen(shlex.split(command))
	else:
		print("Finished Recording")
		p.terminate()

if __name__ == '__main__':
	try:
		setup()
		ledstartup()
		print("Ready")
		thread1 = Thread(target = ledrecording)
		thread2 = Thread(target = ledidle)
		thread1.start()
		thread2.start()
		while True:
			BtnCheck(37)
	except KeyboardInterrupt:
		gpio.cleanup()
		exit()
