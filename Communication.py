from enum import Enum

class Protocol(Enum):
    LoRA = 0
    FSK = 1
class dataSend:
    Protocol = 0
    stop = False
class dataReceive:
    #reciever data
    Protocol = 0
    isConnected = False
    Rssi = 0
    #robot data
    rBatteryVoltage = 0
    rPiTemp = 0
    rCurrentDraw = 0
    rRoll = 0
    rSpeed = 0
class Communication:
    currentProtocol = dataSend.Protocol
    def __init__(self):
        self.protocol = Protocol
    def getProtocol(self):
        return self.protocol(Communication.currentProtocol)
    def getStatus(self):
        return dataReceive.isConnected
    def getRssi(self):
        return dataReceive.Rssi
    