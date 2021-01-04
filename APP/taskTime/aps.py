from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import time

class apsTask():
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.i = 0
    def addTask(self,task):
        taskId = 'id'+str(self.i)
        self.i+=1
        self.scheduler.add_job(task, 'interval', seconds=30,id=taskId)
        self.scheduler.add_job(self.deleteTask, 'interval', seconds=60,id =taskId+'_s', args=[taskId])
    def deleteTask(self,taskId):
        print('停止任务')
        self.scheduler.remove_job(taskId)
        self.scheduler.remove_job(taskId+'_s')
        Job_list=self.scheduler.get_jobs()
        print(Job_list)
        #self.scheduler.start()