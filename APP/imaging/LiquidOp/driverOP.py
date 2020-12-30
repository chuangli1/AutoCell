
import serial
from crc import  *


class Opto():
    def __init__(self):
        self.start()
    def getData(self,data):
        crc = crc16_ibm_calc(data)
        data.append(crc[1])
        data.append(crc[0])
        return data
    def sendCom(self,data):
        self.s.write(data)
    def readData(self):
        return self.s.readline()
    def start(self):
        self.s=serial.Serial(port='COM6', baudrate=115200)
        self.s.write("Start".encode('ascii'))
        if(str(self.readData())[2:7] == 'Ready'): print('连接成功！')
    def close(self):
        #关闭端口
        self.s.close()

    def getTemp(self):
        data = [0x54,0x41]
        data = self.getData(data)
        self.sendCom(data)
        print(self.readData())


if __name__ == "__main__":
    TEST = Opto()
    TEST.getTemp()