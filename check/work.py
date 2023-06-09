# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:06:01 2023

@author: 2023030102
"""
import sys
sys.modules[__name__].__dict__.clear()
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from index_update import index_update
from chn_roi_check import chn_roi

scheduler = BlockingScheduler()

trigger = CronTrigger(day_of_week='mon-fri', hour='16', minute="45", second=0)
# trigger2 = CronTrigger(day_of_week='mon-fri', hour=16, minute=0, second=0)

sched = BlockingScheduler() # 背景執行之排程
sched.add_job(index_update, trigger,id='index_update')
sched.add_job(chn_roi, trigger,id='chn_roi_ok')
sched.start() # 開始