from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

import psycopg2
import pandas as pd
from datetime import datetime,timedelta,date
import requests
import zoneinfo


TW = zoneinfo.ZoneInfo('America/New_York')
datetime(2020, 1, 1, tzinfo=TW)
# calen = pd.read_csv(f'D:/台指期股價/開休市資料.csv',encoding='utf-8') 
# future = pd.read_csv(f'D:/台指期股價/台指期股價_{date}.csv',encoding='utf-8') 

def index_update() :
    def check_daily_constituents(date):
        conn = None
        conn = psycopg2.connect(user='2023030102',
                                    password='jack6025',
                                    host='pg-ndb-twnprc.tejwin.com',
                                    port='5432',
                                    database='twn_prc')
        cursor = conn.cursor()
        future_col = ['zdate', 'open','high','low','close','amt_k']
        
        sql =  f'''         
         select zdate,open,high,low,close,amt_k from prc.index_prc as a left join stk.attr_event as b on a.tej_fp_id = b.tej_fp_id 
    where stk_id = 'Y9999' and zdate = '{date}' --order by zdate
     
                    '''
        cursor.execute(sql)
        future_df = pd.DataFrame(cursor.fetchall(), columns=future_col)
        conn.commit()
        cursor.close()
        df = pd.read_csv('D:/加權指數/台指大盤.csv')
        # date_str = df['zdate'].tail(1).values[0]  # Get the last value from the 'zdate' column
        dft = datetime.strptime(df['zdate'].tail(1).values[0], '%Y-%m-%d')  # Convert the string to a datetime object
        lastday = dft.strftime('%Y%m%d') 
        print(lastday,date)
        # future_df.to_csv(f'D:/加權指數/台指大盤{date}.csv',encoding='utf-8', index=False) 
        if lastday != date : 
            df2 = pd.concat([df,future_df])
            df2.to_csv('D:/加權指數/台指大盤.csv',encoding='utf-8', index=False)
            print('update')
            
            
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
        print("index done")
        default()
    else :
        default_yesterday()
