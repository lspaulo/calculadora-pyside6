import sys
import os
from pathlib import Path

from buttons import ButtonsGrid
from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from styles import setupTheme

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    setupTheme(app)

    icon_path = resource_path(str(WINDOW_ICON_PATH))
    icon = QIcon(icon_path)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()