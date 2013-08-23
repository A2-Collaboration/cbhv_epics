#! /usr/bin/python
#import epics
import time

g = open ("cbhvtestbox19_frompy.sub", "w")

g.write("file \"cbhvtest.db\" \n{\n\tpattern {PROTO, P, BOXNO, LEVELNO, CHANNELNO, ELEMENTNO}\n")


element = 0
level = 0

while (level < 5):
	channel = 0
        while (channel < 8):
		g.write("\t\t{cbhvtest.proto, CB:HV, 19, %s, %s, %s}\n" % (level, channel, element))
		element = element + 1
		channel = channel + 1
	level = level +1

g.write("}")

g.close

