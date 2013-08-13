#! /usr/bin/python

print "hello kph"

level = 0
max = 0
volt = 1400

werte = []

while (level < 5):
    level = level + 1
    channel = 0
    while (channel<8):
        werte.append(volt)
        volt = volt+5
        channel = channel + 1
        max = max + 1

count=0

f = open ("cbhvtestwerte.txt", "w")

while (count < max):
    print (werte[count])
    f.writelines("%s\n" % werte[count])
    count = count + 1
f.close()

