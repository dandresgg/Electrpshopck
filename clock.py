from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
	print('This job is run every one minute.')
	wget http://electroshopckblog.herokuapp.com -O /dev/null


sched.start()