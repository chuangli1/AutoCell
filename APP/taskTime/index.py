#sys.path.append("..")
from .monitorTask import monitorTask
from .regantTask import regantTask
from .aps import apsTask
from monitor.camera import Camera
import time

class taskManager():
    def __init__(self,cap,stage,valves):
        self.apsTask = apsTask()
        self.cap = cap
        self.mi = 0
        self.stage = stage
        self.valves = valves
    def addMonitorTask(self,taskId):
        monitorTaskt = monitorTask(self.cap,self.stage)
        monitorTaskt.initVideo(taskId)
        times = monitorTaskt.times
        interval = int(monitorTaskt.interval[0])
        taskId = str(taskId)+'M'
        self.apsTask.addTask(monitorTaskt.monitorCap,times,interval,taskId,'monitor')
        print('视频任务'+str(taskId)+':'+times[0]+'至'+times[1]+', 任务间隔：'+monitorTaskt.interval[0]+'分')
        self.mi+=1
    def deleteTask(self,taskId,type):
        self.apsTask.deleteTask(taskId,type)
    def addRegantTask(self,taskID):
        regantTaskt = regantTask(self.valves)
        regantTaskt.initRegant(int(taskID))
        times = regantTaskt.times
        interval = int(regantTaskt.interval[0])
        taskId = str(taskID)+'R'
        self.apsTask.addTask(regantTaskt.exeTask,times,interval,taskId,'regant')
        print('试剂任务'+str(taskId)+':'+times[0]+'至'+times[1]+', 任务间隔：'+regantTaskt.interval[0]+'分')



if __name__ == "__main__":
    cap = Camera()
    taskM = taskManager(cap)
    cap.start()
    
    taskM.addMonitorTask(19)
    time.sleep(10)
    taskM.addMonitorTask(19)
   