#!/usr/bin/env python3
import serial
import time
import sys

try:
	filename = sys.argv[1]
except:
	print("you must enter a filename to send!")
	exit(0)


try:
	gcode = open(filename, 'r')
	lines = gcode.readlines()

	ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
	ser.reset_input_buffer()

	for line in lines:
		ser.write(str.encode(line))
		reply = ser.readline().decode('utf-8').rstrip()
		print(reply)
except:
	print("File not found!")
	exit(0)

'''
#define LASER_SSR_OUT_PIN 2
#define GALVO_SSR_OUT_PIN 3
#define LASER_PWM_OUT_PIN 6
const static int pwm_pin_clock = 22;
const static int pwm_pin_sync = 17;  
const static int pwm_pin_dataX = 19;
const static int pwm_pin_dataY = 14;

Only G0 / G1 Supported so far... (linear move commands) G0=without extrusion, G1=with extrusion so G0 is a GOTO and G1 is print at

//M17 - Turn all steppers ON -> Galvo PSU Control (SSR)
//M18 - Turn all steppers OFF -> Galvo PSU Control (SSR)
//M80 - Laser PSU Control (SSR) Implicit delay for SynradCtrl::laserInitTime milliseconds (5000)
//M81 - Laser PSU Control (SSR)


S sets pwm
for example: S200
'''
