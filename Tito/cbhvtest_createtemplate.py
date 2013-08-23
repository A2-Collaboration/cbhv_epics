#! /usr/bin/python
#import epics
import time

f = open ("cbhv_elements.txt", 'r')

werte=f.readlines()

f.close

count = 1

g = open ("cbhvtest_frompy.sub", "w")

g.write("file \"cbhvtest.db\" \n{\n\tpattern {PROTO, P, BOXNO, LEVELNO, CHANNELNO, ELEMENTNO}\n")

while (count<len(werte)):
	zeilenwerte =  werte[count].split()
        if (len(zeilenwerte)==4):
		g.write("\t\t{cbhvtest.proto, CB:HV, %s, %s, %s, %s}\n" % (zeilenwerte[1], zeilenwerte[2], zeilenwerte[3], zeilenwerte[0]))
	count = count + 1

g.write("}")

g.close

