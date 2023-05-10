from PyQt5 import QtWidgets

from controller import SQLQueryApp

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SQLQueryApp()
    window.show()
    sys.exit(app.exec_())
