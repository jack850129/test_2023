import psycopg2
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QTableWidget, QTableWidgetItem, QVBoxLayout
import pandas as pd
from PyQt5.QtCore import QSettings
import sys
sys.stdout.reconfigure(encoding='utf-8')

def sign_sql_chn(username, password):
    global conn
    try:
        conn = psycopg2.connect(
            database='chn',
            user=username,
            password=password,
            host='pg-ndb-chn.tejwin.com',
            port='5432' 
        )
        return conn
    except psycopg2.Error as e:
        print('連線失敗', '無法連線至資料庫: {}'.format(str(e)))
    else:
        return conn

if __name__ == '__main__':
    username = '2023030102'
    password = 'jack6025'
    conn = sign_sql_chn(username, password)
    if conn is not None:
        cur = conn.cursor()
        cur.execute('SELECT * FROM prc.stock_prc limit 10')
        rows = cur.fetchall()
        print('查詢成功')
        conn.close()
    else:
        print('查詢失敗')
