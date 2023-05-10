import psycopg2
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QTableWidget, QTableWidgetItem, QVBoxLayout
import pandas as pd
from PyQt5.QtCore import QSettings
from db_para import sign_sql_chn
from datetime import datetime,timedelta

class SQLQueryApp(QWidget):
    def __init__(self):
        super().__init__()

        # 設定視窗標題、大小、位置
        self.setWindowTitle('SQL Query App')
        self.setGeometry(100, 100, 600, 400)

        # 創建輸入框和標籤
        self.username_label = QLabel('帳號:', self)
        self.username_label.move(20, 20)
        self.username_input = QLineEdit(self)
        self.username_input.move(80, 20)
        self.password_label = QLabel('密碼:', self)
        self.password_label.move(20, 50)
        self.password_input = QLineEdit(self)
        self.password_input.move(80, 50)
        self.password_input.setEchoMode(QLineEdit.Password)

        # 載入儲存的帳號密碼
        self.load_saved_credentials()

        # 連接 returnPressed 信號
        self.username_input.returnPressed.connect(self.run_query)
        self.password_input.returnPressed.connect(self.run_query)

        # 創建執行查詢按鈕
        self.query_button = QPushButton('執行 SQL 查詢', self)
        self.query_button.move(20, 90)
        self.query_button.clicked.connect(self.run_query)

        # 創建顯示查詢結果的文本框
        self.result_textbox = QTextEdit(self)
        self.result_textbox.setGeometry(50, 130, 500, 200)
        self.result_textbox.setReadOnly(True)

        # 創建顯示查詢結果的表格
        self.result_table = QTableWidget(self)
        self.result_table.setFixedSize(500, 200)
        self.result_table.move(50, 130)

        # 顯示視窗
        self.show()

    def load_saved_credentials(self):
        settings = QSettings("MyCompany", "MyApp")
        username = settings.value("username")
        password = settings.value("password")

        if username is not None:
            self.username_input.setText(username)

        if password is not None:
            self.password_input.setText(password)

    def save_credentials(self):
        settings = QSettings('MyCompany', 'MyApp')
        settings.setValue('username', self.username_input.text())
        settings.setValue('password', self.password_input.text())

    def run_query(self):
        # 取得輸入框的值
        username = self.username_input.text()
        password = self.password_input.text()
        # 儲存帳號密碼
        self.save_credentials()
        # 建立連線
        conn = sign_sql_chn(username,password)
        today = datetime.today().strftime('%Y%m%d')    
        # 執行查詢
        try:
            cur = conn.cursor()
            cur.execute(f'''select zdate,count(*),max(keyin) from  chn.prc.margin_cnmgd where zdate>='{str(today)}' group by zdate''')
            rows = cur.fetchall()
            # 將資料填入表格中
            columns = [desc[0] for desc in cur.description]
            self.result_table.setColumnCount(len(columns))
            self.result_table.setHorizontalHeaderLabels(columns)
            self.result_table.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.result_table.setItem(i, j, QTableWidgetItem(str(value)))
            # 調整表格大小
            self.result_table.resizeColumnsToContents()
            self.result_table.resizeRowsToContents()

            # 設定欄位寬度
            self.result_table.setColumnWidth(0, 150)
            self.result_table.setColumnWidth(1, 100)
            # 其他欄位依據需要自行設定
            cur.close()
        except psycopg2.Error as e:
            QMessageBox.critical(self, '查詢失敗', '無法查詢資料: {}'.format(str(e)))
        finally:
            conn.close()


if __name__ == '__main__':
    app = QApplication([])
    sql_query_app = SQLQueryApp()
    app.exec_()
