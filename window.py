from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout
from Communication import Communication

class window(QWidget):
    communication = Communication()
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setWindowTitle("Hoverbot app")
        screen = QApplication.primaryScreen().size()
        self.setGeometry(100, 100, screen.width(), screen.height())
        signalLayout = QHBoxLayout()
        self.signalStrengthLabel = QLabel(f"Signal Strength: {self.communication.getRssi()} dBm RSSI")#fix 0 when able
        self.protocolLabel = QLabel(f"Protocol: {self.communication.getProtocol()}")
        self.statusLabel = QLabel(f"Status: {'Connected' if self.communication.getStatus() else 'Disconnected'}")
        signalLayout.addWidget(self.protocolLabel)        
        signalLayout.addWidget(self.signalStrengthLabel)
        signalLayout.addWidget(self.statusLabel)
        self.layout.addLayout(signalLayout)
        self.layout.addStretch()
        self.setLayout(self.layout)



