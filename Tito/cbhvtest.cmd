dbLoadDatabase "../O.Common/streamApp.dbd"
streamApp_registerRecordDeviceDriver
#streamApp

epicsEnvSet "STREAM_PROTOCOL_PATH", "."

drvAsynIPPortConfigure "termBox19", "10.32.161.119:23"

dbLoadRecords "cbhvtest.db","PROTO=cbhvtest.proto,P=CB:HV,BOXNO=19"
iocInit
var streamDebug 1
