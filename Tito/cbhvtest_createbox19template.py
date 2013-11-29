#! /usr/bin/python
#import epics
import time

g = open ("cbhvtestbox19_frompy.sub", "w")

g.write("file \"cbhvtest.db\" \n{\n\tpattern {PROTO, P, BOXNO, LEVELNO, CHANNELNO, ELEMENTNO, STRINGPOS, INUSE}\n")


element = 720
level = 0
stringpos = "\"%*d"

while (level < 5):

	
	channel = 0
        while (channel < 8):
# uncomment to create output usable to add to a .sub file

		stringpos=stringpos + ",%f\""
		g.write("\t\t{cbhvtest.proto, CB:CB:HV, 19, %s, %s, %s, l%sch%s, yes}\n" % (level, channel, element, level, channel))
	#	g.write("l%sch%s = %s;\n" % (level, channel, stringpos))
		stringpos = stringpos.replace("%f\"", "%*f")
		channel = channel + 1

# uncomment to create output usable for cbhv_elements.txt

	#	g.write("%s\t19\t%s\t%s\n" % (element, level, channel))
		element = element + 1
	#	channel = channel + 1

	stringpos=stringpos + "%*d"

	level = level +1

g.write("}")

g.close

