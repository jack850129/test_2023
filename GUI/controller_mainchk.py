import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication, QShortcut, QTableWidgetItem, QMainWindow, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtWidgets, QtCore
import pandas as pd
from PyQt5.QtCore import QSettings, QRegExp, QDate , QDateTime ,QTimer,QSortFilterProxyModel, QAbstractTableModel
from db_para import Sql_Db_Login
from datetime import datetime,timedelta
from Ui_Login import Ui_Login
from qt_material import apply_stylesheet
# from PyQt5.QtGui import QRegExpValidator,QKeySequence, QIcon
import qt_material
from Ui_Mainchk import Ui_Mainchk
class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Mainchk()
        self.ui.setupUi(self)
        self.setup_control()
        self.setWindowTitle("主檔檢查")
        self.ui.chk_tb.resizeColumnsToContents()


    def setup_control(self):
        self.ui.chk_tb.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        # 毫秒單位
        self.timer.start(1000)  # 隔1秒觸發

    def update_time(self):
        current_datetime = QDateTime.currentDateTime()
        self.ui.Time_edit.setDateTime(current_datetime)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Login = QtWidgets.QWidget()
    window = MainWindowController()
    apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True)
    window.show()
    sys.exit(app.exec_())