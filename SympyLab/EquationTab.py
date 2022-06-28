from .Equation import Equation
import PyQt6.QtWidgets


class EquationTab(PyQt6.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create layout
        self.layout = PyQt6.QtWidgets.QVBoxLayout()

        # add label
        self.label = PyQt6.QtWidgets.QLabel("Equations")

        # add label to layout
        self.layout.addWidget(self.label)

        # add button
        self.button = PyQt6.QtWidgets.QPushButton("Add Equation")

        # add equation when button is clicked
        self.button.clicked.connect(self.add_equation)

        # add button to layout
        self.layout.addWidget(self.button)

        # set layout
        self.setLayout(self.layout)

    def add_equation(self):
        # create equation
        equation = Equation()

        # add equation to the second to last position of the layout
        self.layout.insertWidget(self.layout.count() - 1, equation)
