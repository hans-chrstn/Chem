import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from periodic_table import PeriodicTable

def main():
    # creates the application object
    app = QtWidgets.QApplication([])

    css_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "style.css"))
    # styling the application
    with open(css_path, "r") as file:
        app.setStyleSheet(file.read())

    # creates main window instance
    main_window = PeriodicTable()
    
    # resize
    main_window.resize(900, 900)

    # shows the instance main_window
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

