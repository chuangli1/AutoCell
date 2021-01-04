
from datetime import datetime
class monitorTask():

    def __init__(self, cap):
        self.cap = cap

    def taskWait(self):
        print('t')
        while (True):
           if(self.cap.testCap == 2):
               break
    def initVideo(self,videoName,long):
        self.videoName = videoName
        self.long = long
    def monitorCap(self):
        self.taskWait()
        self.videoNames = self.videoName+datetime.now().strftime(" %Y %m %d %H %M %S")
        self.cap.start_c(self.videoNames,self.long)
