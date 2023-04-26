import sys
sys.modules[__name__].__dict__.clear()
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from index_update import index_update
from chn_roi_check import chn_roi

scheduler = BackgroundScheduler()

trigger = CronTrigger(day_of_week='mon-fri', hour='16', minute="00", second=0)
# trigger2 = CronTrigger(day_of_week='mon-fri', hour=16, minute=0, second=0)

sched = BackgroundScheduler() # 背景執行之排程
sched.add_job(index_update, trigger,id='index_update')
sched.add_job(chn_roi, trigger,id='chn_roi_ok')
sched.start() # 開始