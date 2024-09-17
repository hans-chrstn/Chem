import sys
from PyQt6.QtWidgets import QApplication, QLabel

def main():
    app = QApplication(sys.argv)

    label = QLabel("Does this work or naw")
    label.resize(200, 100)
    label.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

