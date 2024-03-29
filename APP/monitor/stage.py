###author: chuangli 2020-6-16

import serial
import time

MotionChar =["X-","X","Y-","Y","Z-","Z"]
class Stage():

    def __init__(self):

        self.OpenSerial()
        self.autoFocus = None
        self.resetXY('X')
        self.resetXY('Y')
        self.x = 0
        self.y = 0
    def resetXY(self,dir):
        MotionComm = "G28 %s0"%(dir)
        if self.board:
            self.do_commandtest(self.board, MotionComm)
            time.sleep(10)   
            print('%s 方向回零成功'%(dir))
            if(dir=='X'): self.x = 0
            else: self.y = 0

    
    def resetzero(self,x):
        MotionComm = "G28 Z0"
    
        if self.board:
              self.do_commandtest(self.board, MotionComm)
              time.sleep(10)
        self.rotate(100)
        self.MotionCommmand(5,x,200)
        time.sleep(10)
        MotionComm = "G92 Z0"
    
        if self.board:
              self.do_commandtest(self.board, MotionComm)
              time.sleep(5)
        
        print('zero')
        
    def reset(self):
        self.MotionCommmand(5,0,200)
    def changeLocation(self,line,angle):
        MotionComm = "G0 "+MotionChar[3]+str(float(line))+' '+MotionChar[1]+str(angle)+' F'+str(6000)
        print(MotionComm)
        if self.board:
            self.do_commandtest(self.board, MotionComm)
            time.sleep(1)
            self.x = line
            self.y = angle

    def MotionCommmand(self,dir,step,speed):
        #发送位移命令
        self.step = float(step)
        self.speed = int(speed)
        MotionComm = "G0 "+MotionChar[dir]+str(self.step)+' F'+str(60*self.speed)
        print(MotionComm)
        if self.board:
            self.do_commandtest(self.board, MotionComm)
            time.sleep(1)
            if(dir==1): self.x = step
            if(dir==3): self.y = step
    def rotate(self,angle):
        self.MotionCommmand(1,angle,100)
        
    
    def do_commandtest(self, grbl, command, wait=False):
        """
        send the command to grbl, read the response and return it.
        if wait=True, wait for the stepper motion to complete before returning.
        """
        command = command.strip()
        # log().info(">>>> " + command)
        if not command or command[0] == '(':
            return
        commands = command + '\n'
        #commands = '$$'
        grbl.write(commands.encode())
        print(grbl)
        time.sleep(1)
        line = grbl.read_all()
        print(line)
        # log('grbl').info("<<<< "+response)
        # return response
        # 打开串口
    def OpenSerial(self):
        self.board = serial.Serial('/dev/ttyUSB0',115200,timeout=0.5)
        print(self.board.isOpen())
        command="M17\n"
        cmd=command.encode()
        self.board.write(cmd)
        time.sleep(2)
        line = self.board.read_all()
        print(line)
        command="G90\n"
        cmd=command.encode()
        self.board.write(cmd)
        line = self.board.read_all()
        print(line)
    def CloseSerial(self):
        if self.board:
            self.board.close()
            print(self.board.isOpen())
            self.board = None
        