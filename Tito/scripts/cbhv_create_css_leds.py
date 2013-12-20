#! /usr/bin/python

f = open ("cbhvtest_css_demoled.txt", "r")
g = open ("cbhvtest_css_leds.txt", "w")

ledstring = f.read()

f.close

box = 19
level = 0
channel = 0

print ledstring

while box < 20:

    while level < 5:

        while channel < 8:

            xpos = 96 + 36 * channel
            ypos = 138 + 34 * level
            ledstring = ledstring.replace("boxbox", "%d" % box)
            ledstring = ledstring.replace("levellevel", "%d" %  level)
            ledstring = ledstring.replace("channelchannel", "%d" %  channel)
            ledstring = ledstring.replace("xposxpos", "%d" %  xpos)
            ledstring = ledstring.replace("yposypos", "%d" %  ypos)
            g.write("%s" % ledstring)            
            channel = channel + 1

        level = level + 1

    box = box + 1

g.close
