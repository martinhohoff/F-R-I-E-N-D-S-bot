from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def timed_job():
    execfile("app/twitterbot.py)

sched.start()
