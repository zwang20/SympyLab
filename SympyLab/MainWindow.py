import PyQt6.QtWidgets
import PyQt6.QtGui

from .EquationTab import EquationTab


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
        graph = PyQt6.QtGui.QPixmap('graph.png')
        label.setPixmap(graph)
        # widget = PyQt6.QtWidgets.QWidget()
        # layout = PyQt6.QtWidgets.QVBoxLayout()
        # layout.addWidget(label)
        # widget.setLayout(layout)

        # add graph to layout
        self.centralWidget().layout().addWidget(label)
