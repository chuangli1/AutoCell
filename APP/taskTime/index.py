from monitorTask import monitorTask
from aps import apsTask
import sys
sys.path.append("..")
from imaging.camera import Camera
import time


class taskManager():
    def __init__(self,cap):
        self.apsTask = apsTask()
        self.cap = cap
    def addMonitorTask(self,videoName,long):
        monitorTaskt = monitorTask(self.cap)
        monitorTaskt.initVideo(videoName,long)
        self.apsTask.addTask(monitorTaskt.monitorCap)



if __name__ == "__main__":
    cap = Camera()
    taskM = taskManager(cap)
    cap.start()
    
    taskM.addMonitorTask('ls',2)
    time.sleep(10)
    taskM.addMonitorTask('lst',2)
    while True:
        a = 1
        time.sleep(60)
        taskM.apsTask.deleteTask()