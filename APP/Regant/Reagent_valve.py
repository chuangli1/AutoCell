import time
from .pres.pres_control import pres_control
from .pres.MCP23S17 import MCP23S17

class valve_control():
    
    def __init__(self):
        super().__init__()
        self.setup()
    def setup(self):

        #气压模块绑定
        self.MCP = MCP23S17()
        self.MCP.DirGIPOA(0x00)
        self.MCP.DirGIPOB(0x00)
    
    def openvalves(self,channel,valve):
       
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
      
         
if __name__=='main':
    valve = valve_control()
    for i in range(0,8):
      valve.openvalves(i,1)