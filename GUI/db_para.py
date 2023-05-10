import psycopg2
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QTableWidget, QTableWidgetItem, QVBoxLayout
import pandas as pd
from PyQt5.QtCore import QSettings
import sys
sys.stdout.reconfigure(encoding='utf-8')
class Sql_Db_Login : 
    def __init__(self) :
        # self.host = host
        self.username = username
        self.password = password
        # self.database = database
        self.connection = None
    
    def sign_sql_chn(self, username, password):
        try:
            self.connection = psycopg2.connect(
                database='chn',
                user=username,
                password=password,
                host='pg-ndb-chn.tejwin.com',
                port='5432'
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.Error as e:
            print('連線失敗', '無法連線至資料庫: {}'.format(str(e)))
        else:
            return self.connection

    def sign_sql_twnprc(self, username, password):
        try:
            self.connection = psycopg2.connect(
                database='twn_prc',
                user=username,
                password=password,
                host='pg-ndb-twnprc.tejwin.com',
                port='5432'
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.Error as e:
            print('連線失敗', '無法連線至資料庫: {}'.format(str(e)))
        else:
            return self.connection

    def sign_sql_hkg(self, username, password):
        try:
            self.connection = psycopg2.connect(
                database='hkg',
                user=username,
                password=password,
                host='pg-ndb-chn.tejwin.com',
                port='5432'
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.Error as e:
            print('連線失敗', '無法連線至資料庫: {}'.format(str(e)))
        else:
            return self.connection
        
    def sign_sql_jpn(self, username, password):
        try:
            self.connection = psycopg2.connect(
                database='jpn',
                user=username,
                password=password,
                host='pg-ndb-chn.tejwin.com',
                port='5432'
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.Error as e:
            print('連線失敗', '無法連線至資料庫: {}'.format(str(e)))
        else:
            return self.connection
        
    def sign_sql_kor(self, username, password):
        try:
            self.connection = psycopg2.connect(
                database='kor',
                user=username,
                password=password,
                host='pg-ndb-chn.tejwin.com',
                port='5432'
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.Error as e:
            print('連線失敗', '無法連線至資料庫: {}'.format(str(e)))
        else:
            return self.connection


if __name__ == '__main__':
    username = '2023030102'
    password = 'jack6025'
    db_login = Sql_Db_Login()
    cursor = db_login.sign_sql_hkg(username, password)
    if cursor is not None:
        cursor.execute('SELECT * FROM prc.stock_prc limit 10')
        rows = cursor.fetchall()
        print('查詢成功')
        db_login.connection.close()
    else:
        print('查詢失敗')
