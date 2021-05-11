#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import ADS1256#analog to digital
import DAC8532# output pressure
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
DAC = DAC8532.DAC8532()
ADC.ADS1256_init()
def pres_control(pres_set,i):
    
    try:
        DAC = DAC8532.DAC8532()
        kpa1 = pres_set
        temp1 = kpa1/20
        if i==0:
           DAC.DAC8532_Out_Voltage(DAC8532.channel_A,  temp1)
        else:
           DAC.DAC8532_Out_Voltage(DAC8532.channel_B,  temp1)
        time.sleep(2)
    except:
        DAC = DAC8532.DAC8532()
        kpa1 = pres_set / 1.37
        temp1 = kpa1/20
        print(temp1)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 3.7)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 0)
        time.sleep(2)
def pres_read():    
    ADC_Value = ADC.ADS1256_GetAll()
    voltage3 = ADC_Value[0]*5.0/0x7fffff
    print(voltage3)
    kpa_real = (voltage3-0.5)*20/4
    return kpa_real



