import sys
from Communication import Communication
from PyQt5.QtWidgets import QApplication
from Serial import Serial

from window import window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())