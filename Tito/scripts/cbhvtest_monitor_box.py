#! /usr/bin/python

import epics, time, sys, datetime

from epics import caput, caget, PV

now = datetime.datetime.now()

# Check for boxnumber

if len(sys.argv) < 3:

    box = raw_input("Boxnumber:")
    rate = raw_input("Measurementrate[s]:")

else:

    box = sys.argv[1]
    rate = sys.argv[2]

intrate = int(rate)

sys.stdout.write("\x1b]2;Box %s monitor\x07" % box)


# read file

f = open ("cbhv_elements.txt", "r")

werte = f.readlines()

f.close

filename = "box_%s_rate_%s_started_%d-%d-%d_%d.%d.%d.txt" % (box, rate, now.hour, now.minute, now.second, now.day, now.month, now.year)

g = open ("%s" % filename, "w")
g.close

matrix = [[0 for x in xrange(8)] for x in xrange(5)]

while 1:

    count = 1
    
    while (count < len(werte)):

        zeilenwerte = werte[count].split()

        if (len(zeilenwerte) == 4 and zeilenwerte[1] == box):

            matrix[int(zeilenwerte[2])][int(zeilenwerte[3])] = caget ("CB:HV:BOX:%s:%s:%s:read_volt" % (zeilenwerte[1], zeilenwerte[2], zeilenwerte[3]))

            count = count + 1
            
        else:

            count = count + 1

    h = open ("%s" % filename, "a")

    i = 0

#    print "writing now"

    while (i<5):
        
        j = 0

        while (j<8):
        
            h.write("%s\t" % matrix[i][j])

            j = j + 1

        i = i + 1

    h.write("\n")

    h.close

    time.sleep(intrate)
