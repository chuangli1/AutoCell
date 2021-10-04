import sys
#sys.path.append("..")
##sys.path.append("../db")
from datetime import datetime,timedelta
from db.index import findMonitorTasks,addVideos
from monitor.chipCaputer import moveToChip
import time
class monitorTask():
    def __init__(self, cap,stage):
        self.cap = cap
        self.times = [0,0]
        self.interval = [0,0]
        self.location = []
        self.moveToChip = moveToChip(stage)

    def taskWait(self):
        print('任务进入队列')
        while (True):
           if(self.cap.testCap == 2):
               break
    def initVideo(self,taskId):
        #从数据中取task_id = id的数据，拿到视频名称和时长
        videoData = findMonitorTasks(taskId)[0]
        print(videoData)
        if(videoData):
            self.videoName = videoData[1]
            timet = videoData[4].split(",")
            start_dates = (datetime.now()+timedelta(minutes=int(timet[0]))).strftime("%Y-%m-%d %H:%M:%S")
            end_dates = (datetime.now()+timedelta(minutes=int(timet[1]))).strftime("%Y-%m-%d %H:%M:%S")
            self.times = [start_dates,end_dates]
            self.interval = videoData[5].split(",")
            self.long = int(self.interval[1])
            self.userName = videoData[2]
            self.location = videoData[6].split(',')
    def monitorCap(self):
        for i in range(0,len(self.location)):
            location = self.location[i]
            self.moveToChip.moveNext(int(location),self.userName)
            time.sleep(5)
            self.taskWait()
            self.videoNames = self.videoName+'locaiton'+str(location)+datetime.now().strftime(" %Y_%m_%d %H_%M_%S")
            addVideos(self.userName,self.videoNames,datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            self.cap.start_c(self.videoNames,self.long)

