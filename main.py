# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from View.mainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    
    sys.exit(app.exec_())
