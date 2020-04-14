from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import spreadSheet
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
def scheduled_job():
    spreadSheet()

sched.start()