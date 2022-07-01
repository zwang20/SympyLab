import PyQt6.QtWidgets
import sympy
from sympy.parsing.sympy_parser import standard_transformations,\
    implicit_multiplication_application


class Equation(PyQt6.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.equation_left = None
        self.equation_right = None
        self.text = ""

        # create the equation label
        self.equation_text = PyQt6.QtWidgets.QLabel("TODO: Replace with nice latex equation")

        # create text box for the equation
        self.equation_text_box = PyQt6.QtWidgets.QLineEdit()

        # connect the text box to the equation label
        self.equation_text_box.textChanged.connect(self.update_equation)

        # left side
        self.layout_left = PyQt6.QtWidgets.QVBoxLayout()
        self.layout_left.addWidget(self.equation_text)
        self.layout_left.addWidget(self.equation_text_box)
        self.widget_left = PyQt6.QtWidgets.QWidget()
        self.widget_left.setLayout(self.layout_left)

        # create x button
        self.x_button = PyQt6.QtWidgets.QPushButton("x")

        # connect the x button to delete the equation
        self.x_button.clicked.connect(self.deleteLater)

        # create checkbox
        self.checkbox = PyQt6.QtWidgets.QCheckBox()
        # set checkbox to checked
        self.checkbox.setChecked(True)

        # create the layout
        self.layout = PyQt6.QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.checkbox)
        self.layout.addWidget(self.widget_left)
        self.layout.addWidget(self.x_button)

        self.setLayout(self.layout)

    def update_equation(self):
        self.text = self.equation_text_box.text()
        if self.text.count("=") > 1:
            self.text = "Syntax Error"
            self.equation_left = None
            self.equation_right = None
            return
        try:
            lhs, eq, rhs = map(str.strip, self.text.rpartition("="))
            if not eq:
                lhs = "y"
            self.equation_left = sympy.parsing.sympy_parser.parse_expr(
                    lhs,
                    transformations=(*standard_transformations,
                                     implicit_multiplication_application))
            self.equation_right = sympy.parsing.sympy_parser.parse_expr(rhs,
                    transformations=(*standard_transformations,
                                     implicit_multiplication_application))
            self.equation_text.setText(f"{self.equation_left} = {self.equation_right}")
        except (Exception,) as error:
            self.equation_left = None
            self.equation_right = None
            self.equation_text.setText(f"{error}")
