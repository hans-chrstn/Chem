import sys
from PySide6 import QtCore, QtWidgets, QtGui
from periodic_table import PeriodicTable

def main():
    # creates the application object
    app = QtWidgets.QApplication([])

    # styling the application
    with open("style.css", "r") as file:
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

