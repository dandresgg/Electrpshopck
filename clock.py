from apscheduler.schedulers.blocking import BlockingScheduler
from urllib.request import urlopen

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=50)
def timed_job():
	urlopen('https://electroshopckblog.herokuapp.com')


sched.start()