import sys
from PySide6 import QtCore, QtWidgets, QtGui

def main():
    app = QtWidgets.QApplication([])

    label = QtWidgets.QLabel("Does this work or naw")
    label.resize(200, 100)
    label.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

