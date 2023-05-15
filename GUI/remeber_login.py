import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
################################################
#######建立主視窗
################################################
class MainWindow(QMainWindow):
    windowList = []
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setWindowTitle('主介面')
    self.showMaximized()

# 建立選單欄
    self.createMenus()  

def createMenus(self):
    # 建立動作 登出
    self.printAction1 = QAction(self.tr("登出"), self)
    self.printAction1.triggered.connect(self.on_printAction1_triggered)

    # 建立動作 退出
    self.printAction2 = QAction(self.tr("退出"), self)
    self.printAction2.triggered.connect(self.on_printAction2_triggered)

    # 建立選單，新增動作
    self.printMenu = self.menuBar().addMenu(self.tr("登出和退出"))
    self.printMenu.addAction(self.printAction1)
    self.printMenu.addAction(self.printAction2)




# 動作一：登出
def on_printAction1_triggered(self):
    self.close()
    dialog = logindialog()
    if dialog.exec_()==QDialog.Accepted:
        the_window = MainWindow()
        self.windowList.append(the_window)#這句一定要寫，不然無法重新登入
        the_window.show()



# 動作二：退出
def on_printAction2_triggered(self):
    self.close()



# 關閉介面觸發事件
def closeEvent(self, event):
    print(999999999)
    pass

################################################
#######對話方塊
################################################
class logindialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('登入介面')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        ###### 設定介面控制元件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("請輸入賬號")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("請輸入密碼")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.checkBox_remeberpassword = QCheckBox()
        self.checkBox_remeberpassword.setText("記住密碼")
        self.verticalLayout.addWidget(self.checkBox_remeberpassword)

        self.checkBox_autologin = QCheckBox()
        self.checkBox_autologin.setText("自動登入")
        self.verticalLayout.addWidget(self.checkBox_autologin)


        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("確定")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("取消")
        self.verticalLayout.addWidget(self.pushButton_quit)

        ###### 繫結按鈕事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)


        ####初始化登入資訊
        self.init_login_info()



def on_pushButton_enter_clicked(self):
# 賬號判斷
    if self.lineEdit_account.text() == "":
        

    # 密碼判斷
        if self.lineEdit_password.text() == "":
            return


####### 儲存登入資訊
    self.save_login_info()

# 通過驗證，關閉對話方塊並返回1
    self.accept()



# 儲存登入資訊
def save_login_info(self):
    settings = QSettings("config.ini", QSettings.IniFormat)
    settings.setValue("account",self.lineEdit_account.text())
    settings.setValue("password", self.lineEdit_password.text())
    settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
    settings.setValue("autologin", self.checkBox_autologin.isChecked())



# 初始化登入資訊
def init_login_info(self):
    settings = QSettings("config.ini", QSettings.IniFormat)
    the_account =settings.value("account")
    the_password = settings.value("password")
    the_remeberpassword = settings.value("remeberpassword")
    the_autologin = settings.value("autologin")
    ########
    self.lineEdit_account.setText(the_account)
    if the_remeberpassword=="true" or the_remeberpassword==True:
        self.checkBox_remeberpassword.setChecked(True)
        self.lineEdit_password.setText(the_password)

    if the_autologin=="true" or the_autologin==True:
        self.checkBox_autologin.setChecked(True)

    if the_autologin == "true":#防止登出時，自動登入
        threading.Timer(1, self.on_pushButton_enter_clicked).start()
#self.on_pushButton_enter_clicked()

################################################
#######程式入門
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog()
    if dialog.exec_()==QDialog.Accepted:
        the_window = MainWindow()
        the_window.show()
    sys.exit(app.exec_())