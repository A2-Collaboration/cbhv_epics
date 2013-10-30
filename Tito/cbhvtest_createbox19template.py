#! /usr/bin/python
#import epics
import time

g = open ("cbhvtestbox19_frompy.sub", "w")

g.write("file \"cbhvtest.db\" \n{\n\tpattern {PROTO, P, BOXNO, LEVELNO, CHANNELNO, ELEMENTNO, CHAROFFSET}\n")


element = 720
level = 0

while (level < 5):
	channel = 0
        while (channel < 8):

# uncomment to create output usable to add to a .sub file

	#	offset = 67 + 75*level + 9*channel
	#	g.write("\t\t{cbhvtest.proto, CB:HV, 19, %s, %s, %s, %d}\n" % (level, channel, element, offset))

# uncomment to create output usable for cbhv_elements.txt

		g.write("%s\t19\t%s\t%s\n" % (element, level, channel))
		element = element + 1
		channel = channel + 1
	level = level +1

g.write("}")

g.close

