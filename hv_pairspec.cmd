dbLoadDatabase "O.Common/streamApp.dbd"
streamApp_registerRecordDeviceDriver
#streamApp

epicsEnvSet "STREAM_PROTOCOL_PATH", "."

drvAsynIPPortConfigure ("hvp", "10.32.164.20:23")

#dbLoadRecords "hv_pairspec.db","PROTO=hv_pairspec.proto,P=BEAM:PAIRSPEC:HV"
dbLoadTemplate "hv_pairspec.sub"
iocInit
#var streamDebug 1
