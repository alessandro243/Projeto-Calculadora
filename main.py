from PySide6.QtWidgets import QApplication, QLabel
from main_window import Window
from display import Display, Info, Botton, BunttonsGrid
from variables import FILES_DIR
from PySide6.QtGui import QIcon
from styles import setupTheme

import sys

if __name__ == '__main__':

    app = QApplication(sys.argv)
    setupTheme(app)
    window = Window()

    inf = Info('bruh')
    inf.setConfig()
    window.addwidget(inf)

    dis_play = Display()
    dis_play.setConfig()
    dis_play.setStyleSheet('font-size: 30px; font-weight: bold;')
    window.addwidget(dis_play)
    
    grid = BunttonsGrid(dis_play, inf, window)
    window.layout_.addLayout(grid)

    window.setSize()

    icon = QIcon(str(FILES_DIR))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()