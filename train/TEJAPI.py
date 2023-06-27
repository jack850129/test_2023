
import tejapi
import pandas as pd 
import numpy as np 
# import matplotlib.pyplot as plt 
from scipy.stats import norm
# plt.style.use('bmh')
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']

api_key = 'UorqHwXccn4d20DPEmXClMyUFwX832 '
tejapi.ApiConfig.api_key = api_key
tejapi.ApiConfig.ignoretz = True
tejapi.ApiConfig.api_base="http://10.10.10.66"
tejapi.ApiConfig.page_limit=10000


gte, lte = '2022-01', '2023-06'
df1 = tejapi.get('TWN/AINVFINQ',
                   paginate = True,
                  #  coid = '2330',
                    mdate = {'gte':gte, 'lte':lte},
                    	# opts={'pivot':True}
                    # mkt = '',
                   # opts = {
                   #     'columns':[ 'mdate','close_d']
                   # }
                  )
df1.to_csv('D:/API/台灣_量化投資財務分析.csv',encoding='utf-8', index=False)
print(df1)