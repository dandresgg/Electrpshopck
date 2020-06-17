from apscheduler.schedulers.blocking import BlockingScheduler
from urllib.request import urlopen

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
	print('This job is run every one minute.')
	urlopen('https://electroshopckblog.herokuapp.com')


sched.start()