import PyQt6.QtWidgets
import sys


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SympyLab")
        button = PyQt6.QtWidgets.QPushButton("Press Me!")
        self.setCentralWidget(button)


def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
