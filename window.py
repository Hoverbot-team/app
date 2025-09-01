from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QComboBox
from PyQt5.QtCore import QTimer , Qt
from Communication import Communication, dataReceive, Protocol, dataSend
from Serial import Serial
s = Serial()
class window(QWidget):
    communication = Communication()
    def __init__(self):
        super().__init__()
        
        #layouts
        
        self.layout = QVBoxLayout()
        signalLayout = QHBoxLayout()
        upperLayout = QVBoxLayout()

        #window settings
        
        self.setWindowTitle("Hoverbot app")
        screen = QApplication.primaryScreen().size()
        self.setGeometry(100, 100, screen.width(), screen.height())

        #labels
        commLabel = QLabel("Communication")

        #communication related widgets
        
        self.signalStrengthLabel = QLabel(f"Signal Strength: {self.communication.getRssi()} dBm RSSI")
        self.protocolLabel = QLabel(f"Protocol/spreading factor: {self.communication.getProtocol()}")
        self.statusLabel = QLabel(f"Status: {'Connected' if self.communication.getStatus() else 'Disconnected'}")
        self.portSelector = QComboBox()
        self.forcedProtocol = QComboBox()
        
        s.listPorts()
        self.portSelector.addItems(s.devices)
        self.portSelector.currentIndexChanged.connect(lambda: s.init(self.portSelector.currentText()))
        self.forcedProtocol.addItems(Protocol.values())
        self.forcedProtocol.currentIndexChanged.connect(lambda: setattr(dataSend, 'Protocol', self.forcedProtocol.currentIndex()))

        #comms widgets adds

        signalLayout.addWidget(self.portSelector)
        signalLayout.addWidget(self.protocolLabel)        
        signalLayout.addWidget(self.signalStrengthLabel)
        signalLayout.addWidget(self.statusLabel)
        signalLayout.addWidget(self.forcedProtocol)

        #layout adds
        upperLayout.addWidget(commLabel, alignment=Qt.AlignCenter)
        upperLayout.addLayout(signalLayout)
        self.layout.addLayout(upperLayout)
        self.layout.addStretch()
        self.setLayout(self.layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateStatus)
        self.timer.start(500)
    def updateStatus(self):
        self.signalStrengthLabel.setText(f"Signal Strength: {self.communication.getRssi()} dBm RSSI")
        self.protocolLabel.setText(f"Protocol/spreading factor: {self.communication.getProtocol()}")
        self.statusLabel.setText(f"Status: {'Connected' if self.communication.getStatus() else 'Disconnected'}")
        print(dataSend.Protocol)


