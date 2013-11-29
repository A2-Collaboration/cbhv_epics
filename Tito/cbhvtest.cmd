dbLoadDatabase "../O.Common/streamApp.dbd"
streamApp_registerRecordDeviceDriver
#streamApp

epicsEnvSet "STREAM_PROTOCOL_PATH", "."

#drvAsynIPPortConfigure "termBox1", "10.32.161.101:23"
#drvAsynIPPortConfigure "termBox2", "10.32.161.102:23"
#drvAsynIPPortConfigure "termBox3", "10.32.161.103:23"
#drvAsynIPPortConfigure "termBox4", "10.32.161.104:23"
#drvAsynIPPortConfigure "termBox5", "10.32.161.105:23"
#drvAsynIPPortConfigure "termBox6", "10.32.161.106:23"
#drvAsynIPPortConfigure "termBox7", "10.32.161.107:23"
#drvAsynIPPortConfigure "termBox8", "10.32.161.108:23"
#drvAsynIPPortConfigure "termBox9", "10.32.161.109:23"
#drvAsynIPPortConfigure "termBox10", "10.32.161.110:23"
#drvAsynIPPortConfigure "termBox11", "10.32.161.111:23"
#drvAsynIPPortConfigure "termBox12", "10.32.161.112:23"
#drvAsynIPPortConfigure "termBox13", "10.32.161.113:23"
#drvAsynIPPortConfigure "termBox14", "10.32.161.114:23"
#drvAsynIPPortConfigure "termBox15", "10.32.161.115:23"
#drvAsynIPPortConfigure "termBox16", "10.32.161.116:23"
#drvAsynIPPortConfigure "termBox17", "10.32.161.117:23"
#drvAsynIPPortConfigure "termBox18", "10.32.161.118:23"
drvAsynIPPortConfigure "termBox19", "CBHV19.online.a2.kph.:23"

#dbLoadRecords "cbhvtest.db","PROTO=cbhvtest.proto,P=CB:HV,BOXNO=19,LEVELNO=1,CHANNELNO=1"
dbLoadTemplate "cbhvtest.sub"
iocInit
# var streamDebug 1
