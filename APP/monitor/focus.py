from .LiquidOp.driverOP import Opto
from .AutoFocus.AfDemo import AfDemo

class Focus():
    def __init__(self,camera):
        self.dirverOp = Opto()
        self.Af = AfDemo(camera,[20,20,200,200],5000,self.dirverOp)
        self.initCurrent = 0  
    def moveByHand(self,step,dir):
        print(step,dir)
        if(dir=='up'):
            self.initCurrent = step+self.initCurrent
        else:
            self.initCurrent = self.initCurrent-step
        print(self.initCurrent)
        self.dirverOp.setCurrent(self.initCurrent)
    def autoFocus(self):
        print('autoFocus')
        self.Af.start_af(0,20,20,1000,4000,10)
        t = self.dirverOp.getCurrent()
        self.initCurrent = ord(t[1:2])*256+ord(t[2:3])
        print(self.initCurrent)


