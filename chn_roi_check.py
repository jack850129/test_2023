# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:21:32 2023

@author: 2023030102
"""
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import psycopg2
import pandas as pd
from datetime import datetime,timedelta
import requests
import zoneinfo

TW = zoneinfo.ZoneInfo('America/New_York')
datetime(2020, 1, 1, tzinfo=TW)



def chn_roi() :
    def check_daily_constituents(date):
        conn = None
        conn = psycopg2.connect(user='2023030102',
                                    password='jack6025',
                                    host='pg-ndb-hkg.tejwin.com',
                                    port='5432',
                                    database='chn')
        cursor = conn.cursor()
        Idxsample_Col = ['tej_fp_id','stk_id', 'mkt','zdate','roi','clschg','keyin']
        
        sql =  f'''
         
         with t1 as (
        
        select nolimitday.stk_id, nolimitday.list_date,a.tej_fp_id,nolimitday.mkt, nolimitday.mkt_board, a.zdate, nolimitday.nolimitday,preroi,  a.roi, a.ln_roi, a.clschg, a.keyin 
        	from prc.stock_proi as a
           	join (select lag(roi) over (order by tej_fp_id) as preroi ,tej_fp_id,zdate from prc.stock_proi ) as p on a.tej_fp_id = p.tej_fp_id and a.zdate = p.zdate
        	join 
        	(select list.stk_id ,list.tej_fp_id, list.stk_type, list.list_date,b.zdate as nolimitday,list.mkt_board,list.mkt from stk.attr_tradingday as b join 
        		(select c.stk_id,c.tej_fp_id,c.stk_type, c.list_date,d.tradeday_cno,c.mkt,c.mkt_board  from stk.attr_event as c join stk.attr_tradingday d on c.list_date = d.zdate and c.mkt = d.mkt
        		) as list on b.tradeday_cno = list.tradeday_cno+4 and b.mkt = list.mkt
        	) as nolimitday on a.tej_fp_id = nolimitday.tej_fp_id  and a.mkt = nolimitday.mkt
        	where  abs(a.clschg) > 0.02 and a.zdate >= '{str(date)}'  and a.zdate > nolimitday.list_date  and nolimitday.stk_id  not like '3%'  and nolimitday.stk_id  !~ '[A-Za-z]'   and ((abs(roi) >12 and preroi != 0 and nolimitday.mkt_board = '主板' and a.zdate not between  nolimitday.list_date and nolimitday.nolimitday ) or 
        		   (abs(roi) >21 and preroi != 0 and nolimitday.mkt_board != '主板' and a.zdate not between  nolimitday.list_date and nolimitday.nolimitday))
        			order by nolimitday.stk_id,a.zdate
         )
            , 	t2 as(
         select t1.tej_fp_id as tej_fp_id,t1.stk_id ,t1.mkt,t1.zdate,t1.roi,t1.clschg,t1.keyin from t1 left join stk.stk_stkreform  as p on t1.zdate = p.ex_date and t1.stk_id = p.stk_id where ex_date is null 
           )
          , t3 as (
     select t2.tej_fp_id as tej_fp_id ,t2.stk_id,t2.mkt,t2.zdate,t2.roi,t2.clschg,t2.keyin  from t2 
     left join stk.equity_info  as a on t2 .zdate = a.cash_stock_list_date and t2.tej_fp_id = a.tej_fp_id 
     left join stk.equity_sub as c on t2 .zdate = c.ex_date and t2.tej_fp_id = c.tej_fp_id
     where (cash_stock_list_date is null ) and (cash_issue_share is null or cash_issue_share = 0 ) and sub_id is null
     )
      select t3.tej_fp_id as tej_fp_id ,t3.stk_id,t3.mkt,t3.zdate,t3.roi,t3.clschg,t3.keyin  from t3 
     left join stk.equity_info  as a on t3 .zdate = a.stock_list_date and t3.tej_fp_id = a.tej_fp_id 
      where (stock_list_date is null )
                    '''
        cursor.execute(sql)
        Idxsample = pd.DataFrame(cursor.fetchall(), columns=Idxsample_Col)
        conn.commit()
        cursor.close()
        # print(Idxsample)
        if Idxsample.empty is True:
            print(f'{date}中國股價報酬率異常 ... ok')
            Idxsample.to_csv(f'D:/中國股價報酬率檢查/中國股價報酬率檢查OK_{date}.csv',encoding='utf-8', index=False) 
    
        else:
            print(f'{date}中國股價報酬率異常 ... failure')
            Idxsample.to_csv(f'D:/中國股價報酬率檢查/中國股價報酬率檢查ERROR_{date}.csv',encoding='utf-8', index=False) 

            # token = 'PTDxRjB6QyO7N3gA8wrCiwmfS7pNuEMDbLYlEDQbUyL'
            # # 要發送的訊息
            # message = f'{date}中國股價報酬率異常'        
            # # HTTP 標頭參數與資料
            # headers = { "Authorization": "Bearer " + token }
            # data = { 'message': message }                
            # # 以 requests 發送 POST 請求
            # requests.post("https://notify-api.line.me/api/notify",
            #     headers = headers, data = data)
            # Idxsample.to_csv(f'D:/中國股價報酬率檢查/中國股價報酬率檢查ERROR_{date}.csv',encoding='utf-8', index=False) 
    def convert_date(date):
        date = str(int(date[:4])-1911)+'/'+date[4:6]+'/'+date[6:]
        return date
    
    def default():
        today = datetime.today().strftime('%Y%m%d')    
        check_daily_constituents(today)
        
    def default_yesterday():
        today = datetime.today()
        if today.weekday() == 0 :
            yesterday = (today+timedelta(days= -3)).strftime('%Y%m%d')
        else :
            yesterday = (today+timedelta(days= -1)).strftime('%Y%m%d')    
        check_daily_constituents(yesterday)        
        
    # if __name__ == '__main__' :
    judge_time = datetime.now().hour
    if judge_time >= 15 :
        default()
    else :
        default_yesterday()

# def schedulers():
    #排程
trigger = CronTrigger(day_of_week='mon-fri', hour=17, minute=22, second=0)
trigger2 = CronTrigger(day_of_week='mon-fri', hour=17, minute=0, second=0)

sched = BackgroundScheduler() # 背景執行之排程
sched.add_job(chn_roi, trigger,id='chn_roi_ok')
sched.add_job(chn_roi, trigger2,id='chn_roi_ok_2')

sched.start() # 開始
