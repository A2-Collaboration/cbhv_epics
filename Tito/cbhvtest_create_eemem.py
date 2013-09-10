#! /usr/bin/python

f = open("cbhvtest_eememprint.txt", "r")
g = open("cbhvtest.db", "a")
h = open("cbhvtest.proto", "a")
i = open("cbhvtest_monitor_eemem.py", "a")

werte = f.readlines()

f.close

count = 0
string = "%s"

while (count < len(werte)):
    zeilenwert = werte[count].split("=")

    klein = zeilenwert[0].lower()
    gross = zeilenwert[0].upper()

# uncomment to create entries in protocol file

    h.write ("\nread_%s {in \"%s=%s\";} \n\nset_%s {\nout \"eemem unprotect\";\nout \"eemem del %s\";\nout \"eemem add %s %s\";\nout \"eemem protect\";\nout \"eemem print\";\nin \"%s\";\nout \"read_config\";\n}\n" % (klein, gross, string, klein, gross, gross, string, string))

# uncomment to create entries in database file

#    g.write ("\nrecord (stringin, \"$(P):BOX:$(BOXNO):read_%s\")\n{\n    field (DTYP, \"stream\")\n    field (INP, \"@$(PROTO) read_%s termBox$(BOXNO)\")\n    field (SCAN, \"I/O Intr\")\n}\n\nrecord (stringout, \"$(P):BOX:$(BOXNO):set_%s\")\n{\n    field (DTYP, \"stream\")\n    field (OUT, \"@$(PROTO) set_%s termBox$(BOXNO)\")\n    field (PRIO, \"HIGH\")\n}\n" % (klein, klein, klein, klein))

#uncomment to create a script to monitor the pvs

#    i.write ("\n\tcamonitor(\"CB:HV:BOX:19:read_%s\")" % klein)

    count = count + 1

h.close()
g.close()
 
