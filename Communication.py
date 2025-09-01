from enum import Enum

Protocol = {
    0:"FSK",
    1:"SF7",
    2:"SF8",
    3:"SF9",
    4:"SF10",
    5:"SF11" ,
    6 : "SF12"
}

class dataSend:
    Protocol = 0
    stop = False
class dataReceive:
    #reciever data
    Protocol = 0
    isConnected = False
    Rssi = 0
    status = 0
    #robot data
    rBatteryVoltage = 0
    rPiTemp = 0
    rCurrentDraw = 0
    rRoll = 0
    rSpeed = 0
class Communication:
    currentProtocol = dataReceive.Protocol
    def __init__(self):
        self.protocol = Protocol
    def getProtocol(self):
        return Protocol[dataReceive.Protocol]
    def getStatus(self):
        return dataReceive.isConnected
    def getRssi(self):
        return dataReceive.Rssi
    