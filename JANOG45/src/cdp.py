import sys

from pysnmp.hlapi import (
    CommunityData,
    ContextData,
    nextCmd,
    ObjectType,
    ObjectIdentity,
    SnmpEngine,
    UdpTransportTarget
)


PORT = 161
SNMP_COMMUNITY = ""


def walk(host, oid, data, index):
    for i, (errorIndication, errorStatus, errorIndex, varBinds) in \
            enumerate(
                nextCmd(
                    SnmpEngine(),
                    CommunityData(SNMP_COMMUNITY, mpModel=1),
                    UdpTransportTarget((host, PORT)),
                    ContextData(),
                    ObjectType(ObjectIdentity(oid)),
                    lexicographicMode=False
                )
    ):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break
        else:
            for varBind in varBinds:
                data[index].append(str(varBind).split("=")[1])


def cdpneighbor(IP):
    data = [[], [], [], []]
    OID = ".1.3.6.1.4.1.9.9.23.1.2.1.1.6"
    walk(IP, OID, data, 0)
    OID = ".1.3.6.1.4.1.9.9.23.1.2.1.1.7"
    walk(IP, OID, data, 1)
    OID = ".1.3.6.1.4.1.9.9.23.1.2.1.1.8"
    walk(IP, OID, data, 2)
    OID = ".1.3.6.1.4.1.9.9.23.1.2.1.1.9"
    walk(IP, OID, data, 3)
    result = []
    for i in range(len(data[0])):
        result.append(
            {
                "DST-HOST": data[0][i],
                "DST-IF": data[1][i],
                "DST-MODEL": data[2][i],
                "DST-ICON": data[3][i]
            }
        )
    return result
