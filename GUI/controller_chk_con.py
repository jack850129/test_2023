import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication, QShortcut, QTableWidgetItem, QHeaderView, QMainWindow, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtWidgets, QtCore
import pandas as pd
from PyQt5.QtCore import QSettings, QRegExp, QDate , QDateTime ,QTimer , Qt, QSortFilterProxyModel, QAbstractTableModel
from db_para import Sql_Db_Login
from datetime import datetime,timedelta
from Ui_Login import Ui_Login
from qt_material import apply_stylesheet
# from PyQt5.QtGui import QRegExpValidator,QKeySequence, QIcon
import qt_material
from Ui_chk_con import Ui_MainWindow
import numpy as np

class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.setWindowTitle("檢查條件")
        self.ui.tableWidget.resizeColumnsToContents()


    def setup_control(self):
        # self.ui.tableWidget.clear()
        df = pd.read_csv('D:/test_2023/GUI/check_condition_GUI.csv', encoding='Big5')
        self.ui.tableWidget.setRowCount(len(df))
        self.ui.tableWidget.setColumnCount(len(df.columns))

        for i in range(len(df)) :
            for j in range(len(df.columns)) :
                item = QTableWidgetItem(str(df.iloc[i,j]))
                self.ui.tableWidget.setItem(i , j , item)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)


        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(-1) # Search all columns.
        self.proxy_model.setSourceModel(self.ui.tableWidget)

        self.proxy_model.sort(0, Qt.AscendingOrder)

        self.table.setModel(self.proxy_model)

        self.searchbar = QLineEdit()

        # You can choose the type of search by connecting to a different slot here.
        # see https://doc.qt.io/qt-5/qsortfilterproxymodel.html#public-slots
        self.searchbar.textChanged.connect(self.proxy_model.setFilterFixedString)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Login = QtWidgets.QWidget()
    window = MainWindowController()
    apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True)
    window.show()
    sys.exit(app.exec_())