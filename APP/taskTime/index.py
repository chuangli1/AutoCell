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
        print('视频任务'+str(self.mi)+':'+times[0]+'至'+times[1]+', 任务间隔：'+monitorTaskt.interval[0]+'分')
        self.apsTask.addTask(monitorTaskt.monitorCap,times,interval)
        self.mi+=1



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