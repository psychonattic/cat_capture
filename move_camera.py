#!/usr/bin/env python3


#import pantilthat




print( 'type input now: ')


run = True
pan = 0
tilt = 0

pantilthat.pan(pan)
pantilthat.tilt(tilt)

while run:
	str = input()
	if (str == 'w'):
	    print ('up')
	    if(tilt > -90):
	    	tilt -= 1
	if (str == 's'):
	    print ('down')
	    if(tilt < 90):
	    	tilt += 1
	if (str == 'd'):
	    print ('right')
	    if(pan > -90):
	    	pan -= 1
	if (str == 'a'):
	    print ('left')
	    if(pan < 90):
	    	pan += 1
	if (str == 'q'):
	    run = False
	pantilthat.pan(pan)
	pantilthat.tilt(tilt)