from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduler_job('interval', minute=1)
def timed_job():
	print('This job is run every one minute.')


sched.start()