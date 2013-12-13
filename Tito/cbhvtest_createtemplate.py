#! /usr/bin/python
#import epics
import time, sys

# Check for filename

#if len(sys.argv) < 2:

#    box = raw_input('Boxnumber: ')

#else:

#    box = sys.argv[1]

#f = open ("cbhv_all_channel_element_map.txt", 'r')

#werte=f.readlines()

#f.close

g = open ("cbhv2.sub", "w")

#count = 0

#while count < len(werte):

#	zeilenwerte = werte[count].split()
#	element = zeilenwerte[3]
#	box = zeilenwerte[0]
#	level = zeilenwerte[1]
#	channel = zeilenwerte[2]

#	if element == '1000':

#		usage = 0
#	else:
#
#		usage = 1
#
#	g.write("\t\t{cbhvtest.proto, CB:CB:HV, %s, %s, %s, %s, %s}\n" % (box, level, channel, element, usage))
#	g.write("\t\t<pv trig=\"false\">CB:CB:HV:ELEMENT:%s:SetVolt</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:ELEMENT:%s:Channel</pv>\n" % (element, element))
#	count+=1

#g.write("file \"cbhvtest.db\" \n{\n\tpattern {PROTO, P, BOXNO, LEVELNO, CHANNELNO, ELEMENTNO, CHAROFFSET}\n")

#while (count<len(werte)):
#	zeilenwerte =  werte[count].split()

        # uncomment next line to generate .sub file for 1 specific box
        # if (len(zeilenwerte) == 4 and zeilenwerte[1] == box):


       #  uncomment next line to generate .sub file for all boxes
#	if len(zeilenwerte) == 4:
#		level = int(zeilenwerte[2])
#		channel = int(zeilenwerte[3])
#		charoffset = 67 + 75*level + 9*channel
#		g.write("\t\t{cbhvtest.proto, CB:HV, %s, %s, %s, %s, %d}\n" % (zeilenwerte[1], zeilenwerte[2], zeilenwerte[3], zeilenwerte[0], charoffset))

       
        # uncomment next lines to generate text for adding epics pvs to css widgets
#        if (len(zeilenwerte) == 4):

box = 1

while box < 20:

	level = 0

	while level < 5:

		channel = 0

		while channel < 8:

#			g.write("\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:LatestSetVolt</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:InUse</pv>\n" % (box, level, channel, box, level, channel))
#			g.write("\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:SetVolt</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:Element</pv>\n" % (box, level, channel, box, level, channel))
			g.write("\t\t{cbhvtest.proto, CB:CB:HV, %s, %s, %s, N}\n\t\t{cbhvtest.proto, CB:CB:HV, %s, %s, %s, M}\n" % (box, level, channel, box, level, channel))

			channel+=1

		level+=1
	box+=1


        # uncomment the following lines to create testvalues for a file consisting of elements and voltage values seperated via a tab

#count = 0

#while count < 760:

#    g.write("%s\t1500\n" % count)
#    count = count + 1

#g.write("}")

g.close

        

