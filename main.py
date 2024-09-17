import sys
from PySide6 import QtCore, QtWidgets, QtGui

def main():
    # creates the application object
    app = QtWidgets.QApplication([])

    # creates main window instance
    main_window = QtWidgets.QMainWindow()

    # creates a new widget instance
    central_widget = QtWidgets.QWidget()

    # sets the central_widget into the central widget of the main_window instance
    main_window.setCentralWidget(central_widget)

    # creates a layout
    layout = QtWidgets.QVBoxLayout()

    # sets the layout of the central widget
    central_widget.setLayout(layout)

    # creates a label
    label = QtWidgets.QLabel("Does this work???")
    layout.addChildWidget(label)
    
    # sets the title at the title bar of the app
    main_window.setWindowTitle("Project???")

    # resize
    main_window.resize(900, 900)

    # shows the instance main_window
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

