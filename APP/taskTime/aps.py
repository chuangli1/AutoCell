
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import time

class apsTask():
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.i = 0

    def addTask(self,task,times,interval):
        taskId = 'id'+str(self.i)
        self.i+=1
        self.scheduler.add_job(task, 'interval', seconds=interval, start_date =times[0], end_date=time[1], id=taskId)

    def deleteTask(self):
        print('停止任务')
        # self.scheduler.remove_job(taskId)
        # self.scheduler.remove_job(taskId+'_s')
        Job_list=self.scheduler.get_jobs()
        print(Job_list)
        #self.scheduler.start()