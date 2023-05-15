import psycopg2
from PyQt5.QtWidgets import QApplication, QShortcut, QMainWindow, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtWidgets
import pandas as pd
from PyQt5.QtCore import QSettings, QRegExp
from db_para import Sql_Db_Login
from datetime import datetime,timedelta
from Ui_Login import Ui_Login
from qt_material import apply_stylesheet
from PyQt5.QtGui import QRegExpValidator,QKeySequence, QIcon
import qt_material
from Ui_Mainchk import Ui_Mainchk
class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setup_control()
        self.add_shortcut()
        self.setWindowTitle("維護登入")
        self.setWindowIcon(QIcon("icon.png"))

    def setup_control(self):
        self.ui.pushButton_signin.clicked.connect(self.login_check)
        self.ui.lineEdit_password.returnPressed.connect(self.ui.pushButton_signin.click)
        self.ui.lineEdit_account.returnPressed.connect(self.ui.pushButton_signin.click)
        self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)

        # 儲存帳號密碼
        settings = QSettings("TEJ", "GUI")
        savedAccount = settings.value("account")
        savedPassword = settings.value("password")
        if savedAccount is not None:
            self.ui.lineEdit_account.setText(savedAccount)
        if savedPassword is not None:
            self.ui.lineEdit_password.setText(savedPassword)
    # 無鎖定時，點擊Enter觸發登入
    def add_shortcut(self):
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.login_check)   
    # 登入確認檢查        
    def login_check(self) :
        username = self.ui.lineEdit_account.text()
        password = self.ui.lineEdit_password.text()
        if not username or not password:
            QMessageBox.warning(self, 'ERROR' ,"帳號密碼不能為空")
            return    
        self.conn = psycopg2.connect(
                database='chn',
                user=username,
                password=password,
                host='pg-ndb-chn.tejwin.com',
                port='5432'
        )
        
        with self.conn.cursor() as cursor :
            cursor.execute('select * from prc.stock_prc limit 10')
            rows = cursor.fetchall()
            self.conn.commit()
            if len(rows) > 0 : 
                print('OK')
                
            if not rows : 
                print("ERROR") 
                QMessageBox.warning(self, 'ERROR', "登入失敗")      
        if username is not None and password is not None:          
            settings = QSettings("TEJ", "GUI")
            settings.setValue("account", username)
            settings.setValue("password", password)
                  
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Login = QtWidgets.QWidget()
    window = MainWindowController()
    apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True)
    window.show()
    sys.exit(app.exec_())