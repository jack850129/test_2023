
import pandas as pd

# 定義計算移動平均值的函式
def add_ma_columns(df, windows):
    for window_size in windows:
        col_name = f'{window_size}ma'
        df[col_name] = df['close'].rolling(window=window_size).mean()

if __name__ == '__main__' :
    # 讀取數據
    df = pd.read_csv('D:/加權指數/台指大盤.csv', index_col='zdate', parse_dates=True)

    # 計算 10 日、20 日、50 日移動平均值並新增到 df 資料框中
    windows = [10, 20, 50]
    add_ma_columns(df, windows)
    print(df)
