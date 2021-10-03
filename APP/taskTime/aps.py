
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import time
from APP.db.index import deleteTaskLists
from db.index import deleteTaskLists

class apsTask():
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.i = 0
        self.taskList = []

    def addTask(self,task,times,interval,taskId):
        self.taskList.append(taskId)
        print('chuangli',times,interval,taskId)
        self.scheduler.add_job(task, 'interval', minutes=interval, start_date =times[0], end_date=times[1], id=str(taskId))
        self.scheduler.add_job(self.deleteTask, 'date', run_date=times[1], args=[taskId])
    def deleteTask(self,taskID,type):
        print('停止任务'+str(taskID))
        if(type=='monitor'):
            taskId = str(taskID)+'M'
        else:
            taskId = str(taskID)+'R'
        try:
            deleteTaskLists(taskID,type)
            self.taskList.index(taskId)
            self.taskList.remove(taskId)
            self.scheduler.remove_job(str(taskId))
        except:
            pass