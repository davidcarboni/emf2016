import RPi.GPIO as GPIO
import signal
import sys
import threading
import math
from time import sleep
from os import system
from datetime import datetime

THREADS = []
chan_list = []

def cleanup():
	print('cleaning up')
	GPIO.cleanup()

def signal_handler(signal, frame):
	print('Exiting...')
	for t in THREADS:
		t.alive = False
	cleanup()
	sys.exit(0)

def setup():
	global chan_list
	chan_list = [11,12,13,15,16,18,22,7]
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(chan_list, GPIO.OUT)
	global THREADS
	clock = clock_thread()
	clock.start()
	THREADS.append(clock)
	signal.signal(signal.SIGINT, signal_handler)
	while(True):
		signal.pause()

def updatepins(timecode):
	off_list = []
	on_list = []
	print(timecode)
	for x in range(0,8):
		if timecode % 2 == 0:
			off_list.append(chan_list[7 - x])
		else:
			on_list.append(chan_list[7 - x])
		timecode = timecode >> 1
	GPIO.output(on_list, False)
	GPIO.output(off_list, True)

def playhour(timecode):
	GPIO.output(chan_list, False)
	sleep(0.5)
	GPIO.output(chan_list, True)
	sleep(0.5)
	GPIO.output(chan_list, False)
	sleep(0.3)
	for x in range(0, 8):
		sleep(0.2)
		GPIO.output(chan_list[x], True)
	updatepins(timecode)

def playquarter(timecode):
	for y in range(0,5):
		for x in range(1, 8):
			sleep(0.2)
			GPIO.output(chan_list[x-1], True)
			GPIO.output(chan_list[x], False)
		for x in range(7, 0, -1):
			sleep(0.2)
			GPIO.output(chan_list[x], True)
			GPIO.output(chan_list[x-1], False)
	updatepins(timecode)

class clock_thread(threading.Thread):
	def __init__(self):
		self.alive = True
		threading.Thread.__init__(self)


	def run(self):
		while self.alive:
			ctime = datetime.now()
			hour = ctime.hour

			tenmins = int(math.floor(ctime.minute / 10))

			timecode = (hour << 3) + tenmins

			if ctime.minute == 0:
				playhour(timecode)
			elif ctime.minute % 10 == 0:
				playquarter(timecode)
			else:
				updatepins(timecode)

			sleep(60)	
			pass



if __name__ == '__main__':
	setup()

