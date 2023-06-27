
import pandas as pd
import numpy as np 
import polars as pl

df2 = pd.read_csv('D:\\API\\台灣_量化投資財務分析.csv')
# df3 = df2.groupby(['coid'])

con = (df2['coid']==2330)
print(df2.loc[con])
# print(df[df.isnull().T.any()])