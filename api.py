import os
from flask import Flask, request, jsonify
import sys
import threading
import math
from time import sleep
from os import system
from datetime import datetime
import RPi.GPIO as GPIO

THREADS = []
chan_list = []


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "Hello, this is the EMF 2016 number '1' sign! To get started, try a GET to <a href='/lights'>/info</a> or <a href='/lights'>/lights</a>."


@app.route('/info', methods=['GET'])
def info():
    return """This API lets you control the lighs in the nember '1' on the hill above the camp.<br/>
    By default it's a binary clock. The top five lights represent the hour and the bottom three lights are the number of 10-minutes into the hour.<br/>
    You can get make the lights flash by GETting <a href='/lights'>/lights</a> (e.g. in your browser)<br/>"""


@app.route('/lights', methods=['GET'])
def demo():
    for y in range(0,10):
        sleep(0.2)
        for x in range(0, 8):
            if y % 2 = 0:
                if x % 2 = 0:
                    GPIO.output(chan_list[x-1], False)
                else:
                    GPIO.output(chan_list[x-1], True)
            else:
                if x % 2 = 1:
                    GPIO.output(chan_list[x-1], False)
                else:
                    GPIO.output(chan_list[x-1], True)
    updatepins(gettimecode())
    return "Contgratulations. You have made the lights do a little wiggle. Custom lighting sequences coming soon..."


@app.route('/lights', methods=['POST'])
def custom():
    return "Soon this will let you post a custom lighting sequence.."


def setup():
	global chan_list
	chan_list = [11,12,13,15,16,18,22,7]
	GPIO.setmode(GPIO.BOARD)
    GPIO.setup(chan_list, GPIO.OUT)

def start_clock():
	global THREADS
	clock = clock_thread()
    clock.daemon = True
	clock.start()
	THREADS.append(clock)


def updatepins(timecode):
    off_list = []
    on_list = []
    print(timecode)
    for x in range(0, 8):
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
    for y in range(0, 5):
        for x in range(1, 8):
            sleep(0.2)
            GPIO.output(chan_list[x - 1], True)
            GPIO.output(chan_list[x], False)
        for x in range(7, 0, -1):
            sleep(0.2)
            GPIO.output(chan_list[x], True)
            GPIO.output(chan_list[x - 1], False)
    updatepins(timecode)

def gettimecode():
    ctime = datetime.now()
    hour = ctime.hour
    tenmins = int(math.floor(ctime.minute / 10))
    timecode = (hour << 3) + tenmins
    return timecode

class clock_thread(threading.Thread):
	def __init__(self):
		self.alive = True
		threading.Thread.__init__(self)


	def run(self):
		while self.alive:
			ctime = datetime.now()
			timecode = gettimecode()

			if ctime.minute == 0:
				playhour(timecode)
			elif ctime.minute % 10 == 0:
				playquarter(timecode)
			else:
				updatepins(timecode)

			sleep(60)


if __name__ == '__main__':
    setup()
    start_clock()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)