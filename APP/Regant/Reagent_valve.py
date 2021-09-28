import time
from .pres.pres_control import pres_control
from .pres.MCP23S17 import MCP23S17

class valve_control():
    
    def __init__(self):
        super().__init__()
        self.setup()
        self.sourceClose = True;
    def setup(self):

        #气压模块绑定
        self.MCP = MCP23S17()
        self.MCP.DirGIPOA(0x00)
        self.MCP.DirGIPOB(0x00)
    
    def openvalves(self,channel,valve):
        #if(channel==15 and self.sourceClose and valve==1): return
        #valve:0|1
       
        #开关阀门
        if channel<8:
            if valve == 1:
                self.MCP.digitalWrite(channel, 1)
                print('已经打开Channel'+str(channel))
            else: 
                self.MCP.digitalWrite(channel, 0)
                print('已经关闭Channel'+str(channel))
        else:
            if valve == 1:
                self.MCP.digitalWrite(channel, 1)
                print('已经打开Channel'+str(channel))
            else: 
                self.MCP.digitalWrite(channel, 0)
                print('已经关闭Channel'+str(channel))

    def pressure(self,pres_r,i):
        print('启动压力调整程序')
        pres_control(pres_r,i)
    def openSource(self):
        self.openvalves(8,1)
        time.sleep(5)
        self.sourceClose = False
        self.openvalves(15,1)
    def closeSource(self):
        self.openvalves(15,0)
        time.sleep(1)
        self.sourceClose = True
        self.openvalves(8,0)
