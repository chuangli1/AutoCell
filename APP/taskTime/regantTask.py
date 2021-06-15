from datetime import datetime,timedelta
import time
from ..db.index import findRegantTasks
from ..Regant.Reagent_valve import valve_control
class regantTask():
    def __init__(self):
        #初始化
        self.times = [0,0]
        self.interval = [0,0]
        self.valve = []
        self.valveControl = valve_control()
    def taskWait(self):
        print('任务进入队列')
        #排队
    def initRegant(self,taskID):
        #从数据库中拿到数据
        taskD = findRegantTasks(taskID)[0];
        print(taskD)
        if(taskD):
            timet = taskD[5].split(",")
            start_dates = (datetime.now()+timedelta(minutes=int(timet[0]))).strftime("%Y-%m-%d %H:%M:%S")
            end_dates = (datetime.now()+timedelta(minutes=int(timet[1]))).strftime("%Y-%m-%d %H:%M:%S")
            self.times = [start_dates,end_dates]
            self.interval = taskD[7].split(",")
            self.long = int(self.interval[1])
            self.valve = taskD[4].split(',')
    def exeTask(self):
        #执行任务
        for i in range(0,8):
            self.valveControl.openvalves(i,0);
        for i in range(0,len(self.valve)):
            valve = int(self.valve[i]);
            self.valveControl.openvalves(valve,1);
        time.sleep(self.long)
        for i in range(0,8):
            self.valveControl.openvalves(i,0);