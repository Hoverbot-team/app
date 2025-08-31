from enum import Enum

class Protocol(Enum):
    LoRA = 0
    FSK = 1
class dataSend:
    Protocol = 0
    stop = False
class dataReceive:
    Protocol = 0
    isConnected = False
    Rssi = 0
class Communication:
    currentProtocol = dataSend.Protocol
    def __init__(self):
        self.protocol = Protocol
    def getProtocol(self):
        return self.protocol(Communication.currentProtocol)
    def getStatus(self):
        return dataSend.stop
    def getRssi(self):
        return dataReceive.Rssi
    