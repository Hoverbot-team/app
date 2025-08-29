from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout


class window(QWidget):
    layout = QVBoxLayout
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hoverbot app")
        screen = QApplication.primaryScreen().size()
        self.setGeometry(100, 100, screen.width(), screen.height())

