#! /usr/bin/python

f = open ("hvtest.txt", "w")

count = 0

volt = 1370

while (count < 40):

    f.write("%d %d\n" % (count, volt))

    count = count + 1

    volt = volt + 5

f.close
