import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

def job():
    print('Task executed at:', datetime.now())

scheduler = BlockingScheduler()
scheduler.add_job(job, IntervalTrigger(seconds=5), id='my_job_id')
scheduler.start()

while True:
    try:
        pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        sys.exit()
