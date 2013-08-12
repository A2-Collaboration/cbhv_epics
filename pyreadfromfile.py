#! /usr/bin/python
#import epics
import time

f = open ("cbhv-dummywerte", 'r')

werte=f.readlines()

f.close

count = 0

while (count<5):
	print werte[count]
	count = count + 1
	time.sleep(5)

