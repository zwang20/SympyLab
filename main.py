import PyQt6.QtWidgets
import sys


class Equation(PyQt6.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create the equation label
        self.equation = PyQt6.QtWidgets.QLabel("TODO: Replace with nice latex equation")

        # create text box for the equation
        self.equation_text = PyQt6.QtWidgets.QLineEdit()

        # connect the text box to the equation label
        self.equation_text.textChanged.connect(self.update_equation)

        # left side
        self.layout_left = PyQt6.QtWidgets.QVBoxLayout()
        self.layout_left.addWidget(self.equation)
        self.layout_left.addWidget(self.equation_text)
        self.widget_left = PyQt6.QtWidgets.QWidget()
        self.widget_left.setLayout(self.layout_left)

        # create x button
        self.x_button = PyQt6.QtWidgets.QPushButton("x")

        # connect the x button to delete the equation
        self.x_button.clicked.connect(self.deleteLater)

        # create the layout (left = equation, right = x button)
        self.layout = PyQt6.QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.widget_left)
        self.layout.addWidget(self.x_button)

        self.setLayout(self.layout)

    def update_equation(self):
        self.equation.setText(self.equation_text.text())


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

        # add equation to above add equation button
        self.layout.insertWidget(1, equation)


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("SympyLab")

        # create central widget
        central_widget = PyQt6.QtWidgets.QWidget()

        # create layout
        layout = PyQt6.QtWidgets.QHBoxLayout()

        layout.addWidget(EquationTab())
        layout.addWidget(PyQt6.QtWidgets.QLabel('Placeholder Graph'))

        # set central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # create menu bar
        menu_bar = self.menuBar()

        # create menu
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")

        # add menu bar to window
        self.setMenuBar(menu_bar)

        # create colum
        column = PyQt6.QtWidgets.QWidget()
        column.setLayout(PyQt6.QtWidgets.QVBoxLayout())

        #


def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
