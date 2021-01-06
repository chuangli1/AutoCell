import sys
sys.path.append("./taskTime")
from monitorTask import monitorTask
from aps import apsTask
from imaging.camera import Camera
import time


class taskManager():
    def __init__(self,cap):
        self.apsTask = apsTask()
        self.cap = cap
        self.mi = 0
    def addMonitorTask(self,taskId):
        monitorTaskt = monitorTask(self.cap)
        monitorTaskt.initVideo(taskId)
        times = monitorTaskt.times
        interval = int(monitorTaskt.interval[0])
        print('视频任务'+str(taskId)+':'+times[0]+'至'+times[1]+', 任务间隔：'+monitorTaskt.interval[0]+'分')
        self.apsTask.addTask(monitorTaskt.monitorCap,times,interval,taskId)
        self.mi+=1
    def deleteMonitorTask(self,taskId):
        self.apsTask.deleteTask(taskId)



if __name__ == "__main__":
    cap = Camera()
    taskM = taskManager(cap)
    cap.start()
    
    taskM.addMonitorTask(19)
    time.sleep(10)
    taskM.addMonitorTask(19)
    while True:
        a = 1
        time.sleep(60)
        taskM.apsTask.deleteTask()