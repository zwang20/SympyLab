import PyQt6.QtWidgets
import sympy


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
        try:
            if self.text.count("=") == 0:
                self.equation_left = sympy.parsing.sympy_parser.parse_expr("y")
                self.equation_right = sympy.parsing.sympy_parser.parse_expr(self.text)
                self.equation_text.setText("y=" + str(self.equation_right))
            elif self.text.count("=") == 1:
                self.equation_left = sympy.parsing.sympy_parser.parse_expr(self.text.split("=")[0])
                self.equation_right = sympy.parsing.sympy_parser.parse_expr(self.text.split("=")[1])
                self.equation_text.setText(str(self.equation_left) + "=" + str(self.equation_right))
                # TODO
                self.equation_text.setText("TODO: Not implemented")
                self.equation_left = None
                self.equation_right = None
            else:
                self.text = "Syntax Error"
                self.equation_left = None
                self.equation_right = None
        except (Exception,) as error:
            self.equation_text.setText(f"{error}")
            self.equation_left = None
            self.equation_right = None
