dbLoadDatabase "O.Common/streamApp.dbd"
streamApp_registerRecordDeviceDriver
#streamApp

epicsEnvSet "STREAM_PROTOCOL_PATH", "."

drvAsynIPPortConfigure "terminal", "10.32.161.119:23"

dbLoadRecords "test.db","P=TEST"
iocInit
var streamDebug 1
