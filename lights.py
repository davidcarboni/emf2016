import RPi.GPIO as GPIO
import time

def lights():
	chan_list = [11,12,13,15,16,18,22,7]
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(chan_list, GPIO.OUT)
	GPIO.output(chan_list, False)
	time.sleep(0.5)
	GPIO.output(chan_list, True)
	time.sleep(0.5)
	GPIO.output(chan_list, False)
	time.sleep(0.3)
	for x in range(0, 8):
		time.sleep(0.2)
		GPIO.output(chan_list[x], True)
	#for x in range(0, 8):
	#	time.sleep(0.2)
	#	GPIO.output(chan_list[x], False)
	time.sleep(0.5)
	GPIO.output(chan_list[0], False)
	for y in range(0,5):
		for x in range(1, 8):
			time.sleep(0.2)
			GPIO.output(chan_list[x-1], True)
			GPIO.output(chan_list[x], False)
		for x in range(7, 0, -1):
			time.sleep(0.2)
			GPIO.output(chan_list[x], True)
			GPIO.output(chan_list[x-1], False)


	time.sleep(0.2)
	GPIO.cleanup()


if __name__ == '__main__':
    lights()