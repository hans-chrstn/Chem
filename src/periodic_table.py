from PySide6 import QtCore, QtWidgets, QtGui

class ElementButton (QtWidgets.QPushButton):
    def __init__(self, symbol, name, mass, charge, protons, neutrons, electrons):
        super().__init__(symbol)
        self.symbol = symbol
        self.name = name
        self.mass = mass
        self.charge = charge
        self.protons = protons
        self.neutrons = neutrons
        self.electrons = electrons
        self.setStyleSheet("background-color: blue; font-size: 16px;")
        self.clicked.connect(self.info)

    def info(self):
        info = (f"Name: {self.name}\n"
                f"Symbol: {self.symbol}\n"
                f"Mass#: {self.mass}\n"
                f"Charge: {self.charge}\n"
                f"Protons: {self.protons}\n"
                f"Neutrons: {self.neutrons}\n"
                f"Electrons: {self.electrons}\n"
               )
        QtWidgets.QMessageBox.information(None, "Element Info", info)

class PeriodicTable (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Periodic Table")

        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)
        elements = [
            ("H", "Hydrogen", 1.008, 0, 1, 0, 1, 0, 0),
            ("Li", "Lithium", 7, +1, 3, 4, 3, 1, 0),
            ("Be", "Beryllium", 9, 0, 4, 5, 4, 1, 1),
        ]

        for symbol, name, mass, charge, protons, neutrons, electrons, row, col in elements:
            element_button = ElementButton(symbol, name, mass, charge, protons, neutrons, electrons)
            layout.addWidget(element_button, row, col)
            
