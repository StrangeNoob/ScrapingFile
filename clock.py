from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import spreadSheet
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
def scheduled_job():
    spreadSheet()

sched.start()