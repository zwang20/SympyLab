import sys
import traceback

import PyQt6.QtWidgets

import SympyLab


def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    window = SympyLab.MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    try:
        main()
    except (Exception,):
        print(traceback.format_exc())
