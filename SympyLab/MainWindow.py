import os

import PyQt6.QtGui
import PyQt6.QtWidgets

from .EquationTab import EquationTab


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # dry import to deal with first time lag
        from sympy.external.importtools import import_module
        import_module(
            'matplotlib',
            import_kwargs={'fromlist': ['pyplot', 'cm', 'collections']},
            min_module_version='1.1.0',
            catch=(RuntimeError,)
        )

        # set window title
        self.setWindowTitle("SympyLab")

        # create central widget
        central_widget = PyQt6.QtWidgets.QWidget()

        # create layout
        layout = PyQt6.QtWidgets.QHBoxLayout()

        layout.addWidget(EquationTab())

        # add graph
        layout.addWidget(PyQt6.QtWidgets.QLabel('Placeholder Graph'))

        # set central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # create menu bar
        self.menu_bar = self.menuBar()

        # create menu
        file_menu = self.menu_bar.addMenu("File")
        edit_menu = self.menu_bar.addMenu("Edit")

        # add menu bar to window
        self.setMenuBar(self.menu_bar)

    def refresh(self):

        # delete last widget in layout
        for widget in self.centralWidget().children():
            if type(widget) != PyQt6.QtWidgets.QLabel:
                continue
            widget: PyQt6.QtWidgets.QLabel = widget
            widget.deleteLater()

        label = PyQt6.QtWidgets.QLabel()
        graph = PyQt6.QtGui.QPixmap(os.path.join("cache", "graph.png"))
        label.setPixmap(graph)

        # add graph to layout
        self.centralWidget().layout().addWidget(label)
