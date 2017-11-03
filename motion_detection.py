#!/usr/bin/env python3
#above line allows to be run from command line without python command
import picamera
from subprocess import call #makes it possible to execute bash commqands from the program

PATH = '/home/pi/Desktop/pi_camera/'
EXT = '.h264'



def recordVideo(name):
	camera = picamera.PiCamera()
	camera.resolution = (640, 480)
	camera.start_recording(PATH + name + EXT)
	camera.wait_recording(5)
	camera.stop_recording()
	bashCommand('MP4Box -add ' + name + EXT + ' ' + name + '.mp4')

def bashCommand(command):
	call ([command], shell=True)

recordVideo('Joel')