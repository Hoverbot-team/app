from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setWindowTitle("Hoverbot app")
        screen = QApplication.primaryScreen().size()
        self.setGeometry(100, 100, screen.width(), screen.height())
        self.signalStrengthLabel = QLabel(f"Signal Strength: {0}")
        self.layout.addWidget(self.signalStrengthLabel)
        self.setLayout(self.layout)



