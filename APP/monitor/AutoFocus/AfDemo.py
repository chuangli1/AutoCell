# simple GUI for demonstration purposes of autofocus functionality
# coding: utf-8
# author: chuangli 2020-7-14

import numpy as np
import cv2
import sys
from . import peak_search_lense_final as psl
import time


class AfDemo():
    def __init__(self,cap,aoi,zero,stage):
        """
        cap: opencv摄像头
        aoi: 感兴趣区域坐标数组[x1,y1,x2,y2]
        zero: 零点距离限位的高度
        stage: 位移控制类
        """
       
        #绑定摄像头
        self.cam = cap
        #确定对焦区域
        self.roi = aoi
        #绑定位移控制并归零
        self.lc = stage
        #self.lc.resetzero(zero)

        self.afX = 0
        self.afY = 0
        self.afN = 0
    

    def start_af(self,algorithm,cStep,fStep,start,stop,hyst):
        """
        cStep: 二步算法的步长参数
        ftSep: 单步步长
        start: 对焦起始位置
        stop: 对焦终止位置
        hyst: 补偿滞后的偏移量
        """
        if algorithm == 0:
            # Global peak single step algorithm.
            print(psl.global_peak_single_step)
            self.afX, self.afY, self.afN = psl.global_peak_single_step(
                                                            self.cam,
                                                            self.lc,
                                                            fStep,
                                                            start,
                                                            stop,
                                                            self.roi)
            self.afX -= hyst  # add hysteresis
        elif algorithm == 1:
            # Global peak two step algorithm.
            self.afX, self.afY, self.afN = psl.global_peak_two_step(
                                                            self.cam,
                                                            self.lc,
                                                            cStep,
                                                            fStep,
                                                            start,
                                                            stop,
                                                            self.roi,
                                                            hyst)
            self.afX -= hyst  # add hysteresis
        elif algorithm == 2:
            # Fibonacci algorithm.
            self.afX, self.afY, self.afN = psl.fibonacci_peak(
                                                            self.cam,
                                                            self.lc,
                                                            start,
                                                            stop,
                                                            self.roi,
                                                            hyst,
                                                            4)
       
        print('focus pos:',self.afX)
        self.lc.go_to_position(self.afX)
        time.sleep(1)
