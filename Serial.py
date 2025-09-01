import threading
from Communication import Protocol, dataReceive
import serial
import time
import struct
import serial.tools.list_ports

class Serial():
    ser = None
    devices = []
    def listPorts(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.devices.append(port.device)
            print(self.devices)
    def init(self, port):
        try:
            ser = serial.Serial(port, 115200) 
            self.ser = ser
            self.thread = threading.Thread(target=self.readSerial, daemon=True)
            self.thread.start()
            print("Serial port initialized")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
    def readSerial(self):
        while True:
            if self.ser.in_waiting >= 7: 
                data = self.ser.read(7)   
                protocol, isConnected, Rssi, status = struct.unpack('=b?fB', data)
                dataReceive.Protocol = protocol
                dataReceive.isConnected = isConnected
                dataReceive.Rssi = Rssi
                dataReceive.status = status
    