
import serial
from .crc import  crc16_ibm_calc


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
        
        self.s=serial.Serial('/dev/ttyACM0',115200,timeout=0.5)
        self.s.write("Start".encode('ascii'))
        if(str(self.readData())[2:7] == 'Ready'): print('液体镜头连接成功！')
    def close(self):
        #关闭端口
        self.s.close()
    def getTemp(self):
        data = [0x54,0x41]
        data = self.getData(data)
        self.sendCom(data)
        return self.readData()
    def setCurrent(self,value):
        data = [0x41,0x77]
        values = value.to_bytes(2, byteorder='big')
        data.append(values[0])
        data.append(values[1])
        data = self.getData(data)
        self.sendCom(data)
    def getCurrent(self):
        data = [0x41,0x72,0x00,0x00,0xb4,0x27]
        self.sendCom(data)
        return self.readData()
    def go_to_position(self,value):
        self.setCurrent(value)
    def resetzero(self):
        self.setCurrent(0)



if __name__ == "__main__":
    TEST = Opto()
    TEST.getTemp()
    TEST.setCurrent(1234)
    TEST.getTemp()