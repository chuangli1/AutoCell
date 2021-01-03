from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import time

class apsTask():
    def __init__(self):
        self.scheduler = BackgroundScheduler()
    def addTask(self,task):
        self.scheduler.add_job(task, 'interval', seconds=2)
        self.scheduler.start()
    def deleteTask(self,task):
        self.scheduler.add_job(task, 'interval', seconds=3)
        #self.scheduler.start()

def job():
    print(1)
def job2():
        print(13)
if __name__ == "__main__":
    aps = apsTask()
    aps.addTask(job)
    time.sleep(1)
    aps.deleteTask(job2)
    while True:
        a = 1