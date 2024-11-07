from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QMainWindow, QVBoxLayout, QWidget

class Window(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.center = QWidget()
        self.layout_ = QVBoxLayout()
        self.center.setLayout(self.layout_)
        self.setCentralWidget(self.center)

        self.setWindowTitle('Calculadora')

    def addwidget(self, label: QWidget):
        self.layout_.addWidget(label)

    def setSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def makeMsgBox(self):
        return QMessageBox(self)