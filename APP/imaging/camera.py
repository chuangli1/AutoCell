# -*- coding: utf-8 -*-
import cv2
import shutil
import time
import threading
from functools import partial

def gen(camera):
    camera.userNum+=1
    if camera.userNum==1:
        camera.resume()
        time.sleep(0.01)
    while True:
        frame = camera.frame
        ret, frame = cv2.imencode('.jpg', frame)
        try:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')
        except:
            camera.pause()
            break
def genVideo(videoName):
    cap = cv2.VideoCapture('../video/'+videoName)
    while True:
        ret, frame = cap.read()
        if(ret==False):
           break
        ret, frame = cv2.imencode('.jpg', frame)
        try:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')
            time.sleep(0.03)
        except:
            cap.release()
            break


class Camera(threading.Thread):
    def __init__(self):
        super(Camera,self).__init__()
        self.__flag = threading.Event() 
        self.__flag.set()       # 设置为True
        self.userNum = 0
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True
        self.test = 2 #验证是否进行视频拍摄
        self.cap = cv2.VideoCapture(0)
        ret,self.frame = self.cap.read()
        self.capWidth = int(self.cap.get(3))
        print(self.capWidth)
        self.capHeight = int(self.cap.get(4))
        print(self.capHeight)
        self.cap.release()
        self.out = 0
        self.i = 0
    def start_c(self,videoName):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('../video/'+videoName+'.avi',fourcc, 20.0, (self.capWidth,self.capHeight),True)
        self.test = 1
        self.i = 0
        print('开始拍摄，将视频写入文件')
    def stop_c(self):
        self.test = 0
        print('停止将视频写入文件')
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()
            ret,self.frame = self.cap.read()
            #cv2.imshow('img',self.frame)
            if self.test == 1:
                self.out.write(self.frame)
            if self.test == 0:
                self.out.release()
                print('chuangli')
                self.test = 2
            self.i+=1
            time.sleep(0.05)
        print('stop')

    def pause(self):
        self.userNum-=1
        if self.userNum>0:
            pass
        else:
            self.__flag.clear()     # 设置为False, 让线程阻塞
            self.cap.release()  #常规操作
            print('close camera')
    def resume(self):
        self.cap = cv2.VideoCapture(0)
        ret,self.frame = self.cap.read()
        time.sleep(0.1)
        self.__flag.set()    # 设置为True, 让线程停止阻塞
        print('open camera')
    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False
        print(self.__running.isSet())
        print('close camera')
    