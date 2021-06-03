###author: chuangli 2020-6-16

import serial
import time

MotionChar =["X-","X","Y-","Y","Z-","Z"]
class Stage():

    def __init__(self):

        self.OpenSerial()
    
    def resetzero(self,x):
        MotionComm = "G28 Z0"
    
        if self.board:
              self.do_commandtest(self.board, MotionComm)
              time.sleep(10)
        self.MotionCommmand(5,x,200)
        time.sleep(10)
        MotionComm = "G92 Z0"
    
        if self.board:
              self.do_commandtest(self.board, MotionComm)
              time.sleep(5)
        
        print('zero')
        
    def reset(self):
        self.MotionCommmand(5,0,200)

    def MotionCommmand(self,dir,step,speed):
        #用于手动扫描
        self.step = float(step)
        self.speed = int(speed)
        MotionComm = "G0 "+MotionChar[dir]+str(self.step)+' F'+str(60*self.speed)
        print(dir)
        if self.board:
              self.do_commandtest(self.board, MotionComm)
              time.sleep(0.5)
    def go_to_position(self,x):
        self.MotionCommmand(5,x/3200,200)
        print('x ', x/3200)
    def rotate(self,angle):
        command = "G1 X" + str(angle) +'\n'
        if self.board:
              self.do_commandtest(self.board, command)
              time.sleep(2)
        
    
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
        