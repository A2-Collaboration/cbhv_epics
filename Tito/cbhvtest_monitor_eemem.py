#! /usr/bin/python

import epics

from epics import camonitor

while 1:

	camonitor("CB:HV:BOX:19:read_dhcp")
	camonitor("CB:HV:BOX:19:read_ip")
	camonitor("CB:HV:BOX:19:read_mask")
	camonitor("CB:HV:BOX:19:read_gate")
	camonitor("CB:HV:BOX:19:read_dns")
	camonitor("CB:HV:BOX:19:read_ntpserver")
	camonitor("CB:HV:BOX:19:read_utczone")
	camonitor("CB:HV:BOX:19:read_r1")
	camonitor("CB:HV:BOX:19:read_r2")
	camonitor("CB:HV:BOX:19:read_ntp")
	camonitor("CB:HV:BOX:19:read_umin")
	camonitor("CB:HV:BOX:19:read_levels")
	camonitor("CB:HV:BOX:19:read_neg")
	camonitor("CB:HV:BOX:19:read_mem")
	camonitor("CB:HV:BOX:19:read_file")
	camonitor("CB:HV:BOX:19:read_reg_div")
	camonitor("CB:HV:BOX:19:read_cards")
	camonitor("CB:HV:BOX:19:read_m0")
	camonitor("CB:HV:BOX:19:read_n0")
	camonitor("CB:HV:BOX:19:read_m1")
	camonitor("CB:HV:BOX:19:read_n1")
	camonitor("CB:HV:BOX:19:read_m2")
	camonitor("CB:HV:BOX:19:read_n2")
	camonitor("CB:HV:BOX:19:read_m3")
	camonitor("CB:HV:BOX:19:read_n3")
	camonitor("CB:HV:BOX:19:read_m4")
	camonitor("CB:HV:BOX:19:read_n4")
	camonitor("CB:HV:BOX:19:read_umax")
	camonitor("CB:HV:BOX:19:read_mac")
	camonitor("CB:HV:BOX:19:read_lease")
	camonitor("CB:HV:BOX:19:read_reg")
	camonitor("CB:HV:BOX:19:read_regn")
	camonitor("CB:HV:BOX:19:read_write_protect")