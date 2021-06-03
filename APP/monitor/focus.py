from .LiquidOp.driverOP import Opto

class Focus():
    def __init__(self):
        self.dirverOp = Opto()
        self.initCurrent = 0  
    def moveByHand(self,step,dir):
        if(dir=='up'):
            self.initCurrent = step+self.initCurrent
        else:
            self.initCurrent = self.initCurrent-step
        self.dirverOp.setCurrent(self.initCurrent)

