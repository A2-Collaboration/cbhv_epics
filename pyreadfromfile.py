#! /usr/bin/python

gelesen = []

f = open ("cbhvtestwerte.txt", "r")

count = 0
testcount = 0
max = len(f.readline())
print max
line = f.readline(count)

if not line==0:
    line = f.readline(count)
    print line
    gelesen.append(line)
f.close

# while (testcount < max):
# print (gelesen)
         # testcount = testcount + 1

