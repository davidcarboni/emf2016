#!/bin/sh
# launcher.sh

sudo pkill python
cd /home/pi/git/emf2016
nohup sudo python api.py &
