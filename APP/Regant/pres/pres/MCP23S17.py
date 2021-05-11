#!/usr/bin/python

import time
import math
import RPi.GPIO as GPIO

class MCP23S17():
    def __init__(self,MISO=26,MOSI=19,CLK=13,CS=12,RESET=5):
        self.ADDR = 0b0100000
        self.IODIRA = 0x00
        self.IODIRB = 0x01
        self.GPIOA  = 0x12
        self.GPIOB  = 0x13
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.MISO   = MISO
        self.MOSI   = MOSI
        self.CLK    = CLK
        self.CS     = CS
        self.RESET  = RESET
        GPIO.setup(self.MISO, GPIO.IN)
        GPIO.setup(self.MOSI, GPIO.OUT)
        GPIO.setup(self.CLK, GPIO.OUT)
        GPIO.setup(self.CS, GPIO.OUT)
        GPIO.setup(self.RESET, GPIO.OUT)
        self.Reset()
        self.CsHigh()
        self.ClkLow()
        self.MosiLow()
        #self.WriteReg(self.IODIRA,0)
        #self.WriteReg(self.IODIRB,0)
        'initialize'
        #self.WriteGPIOA(0x00)
        #self.WriteGPIOB(0x00)
        self._GPIOA = 0
        self._GPIOB = 0
    def Reset(self):
        GPIO.output(self.RESET,False)
        time.sleep(0.1)
        GPIO.output(self.RESET,True)
        time.sleep(0.1)
    def CsLow(self):
        GPIO.output(self.CS,False)
    def CsHigh(self):
        GPIO.output(self.CS,True)
    def ClkLow(self):
        GPIO.output(self.CLK,False)
    def ClkHigh(self):
        GPIO.output(self.CLK,True)
    def MosiLow(self):
        GPIO.output(self.MOSI,False)
    def MosiHigh(self):
        GPIO.output(self.MOSI,True)
    def SpiSend(self,data):
        for i in range(8):
            if data & 0b10000000:
                self.MosiHigh()
            else:
                self.MosiLow()
            time.sleep(0.001)
            self.ClkHigh()
            time.sleep(0.001)
            self.ClkLow()
            time.sleep(0.001)
            data <<= 1
    def WriteReg(self,regaddr,data):
        IC_addr = (self.ADDR << 1) | 0
        REG_addr = regaddr
        self.CsLow()
        self.SpiSend(IC_addr)
        self.SpiSend(REG_addr)
        self.SpiSend(data)
        self.CsHigh()

    def ReadReg(self,regaddr):
        # IC_addr = 0b01000001
        IC_addr = (self.ADDR << 1) | 1
        REG_addr = regaddr
        self.CsLow()
        self.SpiSend(IC_addr)
        self.SpiSend(REG_addr)
        data = 0
        for i in range(8):
            data = data << 1
            if GPIO.input(self.MISO) == True:
                data |= 1
            else:
                data &= ~1
            self.ClkHigh()
            time.sleep(0.001)
            self.ClkLow()
            time.sleep(0.001)
        self.CsHigh()
        return data
    def DirGIPOA(self,value):
        self.WriteReg(self.IODIRA,value)
    def DirGIPOB(self,value):
        self.WriteReg(self.IODIRB,value)
    def ReadGPIOA(self):
        return int(math.log(self.ReadReg(self.GPIOA),2))
    def WriteGPIOA(self,value):
        self.WriteReg(self.GPIOA,value)
    def ReadGPIOB(self):
        return int(math.log(self.ReadReg(self.GPIOB), 2))
    def WriteGPIOB(self,value):
        self.WriteReg(self.GPIOB,value)
    def Write_A(self, value):
        assert value>=0 and value<=7
        v = 2**value
        self.WriteReg(self.GPIOA, v)
    def Write_B(self, value):
        assert value>=0 and value<=7
        v = 2**value
        self.WriteReg(self.GPIOB, v)
    def digitalWrite(self, pin, level):
        'set the level of a given pin'
        assert(pin<16)
        assert(level==0) or (level==1)
        if pin<8:
            register = self.GPIOA
            noshifts = pin
            data = self._GPIOA
        else:
            register = self.GPIOB
            noshifts = pin & (0x07)
            data = self._GPIOB
        if level == 1:
            data |= (1<<noshifts)
        else:
            data &= (~(1<<noshifts))
        self.WriteReg(register, data)
        if pin<8:
            self._GPIOA = data
        else:
            self._GPIOB = data
    def readGPIO(self):
        'read the data port value of all pins'
        data = (self.ReadReg(self.GPIOA)) | (self.ReadReg(self.GPIOB)<<8)
        retpin = []
        for i in range(16):
            if ((data>>i) &1):
                retpin.append(i)
        return retpin