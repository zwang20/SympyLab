import os
import traceback

import PyQt6.QtWidgets
import sympy

from .Equation import Equation

import matplotlib.colors as mcolors


class EquationTab(PyQt6.QtWidgets.QWidget):
    colors = tuple(mcolors.TABLEAU_COLORS.keys())

    def __init__(self):
        super().__init__()

        # create layout
        self.plot = None
        self.layout = PyQt6.QtWidgets.QVBoxLayout()

        # add label
        self.label = PyQt6.QtWidgets.QLabel("Equations")

        # add label to layout
        self.layout.addWidget(self.label)

        # add button
        self.button = PyQt6.QtWidgets.QPushButton("Add Equation")

        # add equation when button is clicked
        self.button.clicked.connect(self.add_equation)

        self.refresh_button = PyQt6.QtWidgets.QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)

        # add button to layout
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.refresh_button)

        # set layout
        self.setLayout(self.layout)

    def add_equation(self):
        # create equation
        equation = Equation()

        # add equation to the second to last position of the layout
        self.layout.insertWidget(self.layout.count() - 2, equation)

    def refresh(self):

        # loop over all Equation
        plot = None
        for color, equation in zip(self.colors, self.children()):

            if type(equation) != Equation:
                continue
            equation: Equation = equation
            if equation.equation_right is None:
                continue
            lhs, rhs = equation.equation_left, equation.equation_right
            for f in sympy.solve(lhs - rhs, sympy.var("y")):
                if plot is None:
                    plot = sympy.plotting.plot(
                            f,
                            show=False,
                            line_color=color,
                            ylabel="y")
                else:
                    plot.extend(sympy.plotting.plot(
                            f,
                            show=False,
                            line_color=color,
                            ylabel="y")
                    )
        if plot is not None:
            if not os.path.exists("cache"):
                os.mkdir("cache")
            plot.save(os.path.join("cache", "graph.png"))
            self.plot = plot
            self.parent().parent().refresh()
