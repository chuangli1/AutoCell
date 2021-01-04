
from datetime import datetime,timedelta
class monitorTask():

    def __init__(self, cap):
        self.cap = cap

    def taskWait(self):
        print('任务进入队列')
        while (True):
           if(self.cap.testCap == 2):
               break
    def initVideo(self,videoName,long):
        #从数据中取task_id = id的数据，拿到视频名称和时长
        self.videoName = videoName
        self.long = long
        start_dates = (datetime.now()+timedelta(seconds=30)).strftime("%Y-%m-%d %H:%M:%S")
        end_dates = (datetime.now()+timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")
        self.times = [start_dates,end_dates]
        self.interval = [0,0]
        self.long = self.interval[1]
    def monitorCap(self):
        self.taskWait()
        self.videoNames = self.videoName+datetime.now().strftime(" %Y %m %d %H %M %S")
        self.cap.start_c(self.videoNames,self.long)
