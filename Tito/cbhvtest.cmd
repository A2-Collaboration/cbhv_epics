dbLoadDatabase "../O.Common/streamApp.dbd"
streamApp_registerRecordDeviceDriver
#streamApp

epicsEnvSet "STREAM_PROTOCOL_PATH", "."

drvAsynIPPortConfigure "termBox1", "CBHV01.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox2", "CBHV02.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox3", "CBHV03.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox4", "CBHV04.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox5", "CBHV05.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox6", "CBHV06.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox7", "CBHV07.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox8", "CBHV08.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox9", "CBHV09.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox10", "CBHV10.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox11", "CBHV11.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox12", "CBHV12.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox13", "CBHV13.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox14", "CBHV14.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox15", "CBHV15.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox16", "CBHV16.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox17", "CBHV17.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox18", "CBHV18.online.a2.kph.:23"
drvAsynIPPortConfigure "termBox19", "CBHV19.online.a2.kph.:23"

#dbLoadRecords "cbhvtest.db","PROTO=cbhvtest.proto,P=CB:HV,BOXNO=19,LEVELNO=1,CHANNELNO=1"
dbLoadTemplate "cbhvtest.sub"
iocInit
# var streamDebug 1
