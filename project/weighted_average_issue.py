from db_para import Sql_Db_Login
import psycopg2
import pandas as pd
import polars as pl

username = '2023030102'
password = 'Jack6025'
login = Sql_Db_Login()
# cursor = login.sign_sql_twn(username, password)
# cursor.execute('''select * from 	fin.fin_finstat_ma  where acc_code in ('3990','211F','7210','3950','240D','240E','240G') 
# ''')
# rows = cursor.fetchall()
# # 取得查詢結果的欄位名稱
# column_names = [desc[0] for desc in cursor.description]

# # 將資料轉換為 DataFrame
# df = pd.DataFrame(rows, columns=column_names)

# # 關閉連線
# cursor.close()

# login.connection.close()
# print(df)
# df.to_csv('D:/WAISFIN.csv',encoding='utf-8', index=False)

# --------------

cursor = login.sign_sql_twnprc(username, password)
cursor.execute('''
select a.tej_fp_id , stk_id,tej_comp_id,stk_type,close ,zdate,c.stk_ex_date,pre_close,ex_price,issue_share_tej,cashback,adjfac_type,j,adj,cap_dec_share,	cap_dec_share_amt,c.issue_price,c.pre_ex_total_share,c.stkcap_total_share
from prc.stock_prc as a 
left join stk.attr_event as b on a.tej_fp_id=b.tej_fp_id 
left join Prc.stock_adjfac as e on a.tej_fp_id=e.tej_fp_id and  a.zdate = e.ex_date
left join stk.stk_stkinta as c on a.tej_fp_id = c.tej_fp_id  and a.zdate = c.stk_ex_date
left join stk.stk_stkintb as d on a.tej_fp_id = d.tej_fp_id  and a.zdate = d.stk_ex_date
where   c.stk_ex_date is not null and stk_type in ('1','2','B') --and c.pre_ex_total_share is null
order by zdate desc,a.tej_fp_ID
''')
rows = cursor.fetchall()
# 取得查詢結果的欄位名稱
column_names = [desc[0] for desc in cursor.description]

# 將資料轉換為 DataFrame
df = pd.DataFrame(rows, columns=column_names)

# 關閉連線
cursor.close()

login.connection.close()
print(df)
df.to_csv('D:/WAIS.csv',encoding='utf-8', index=False)
