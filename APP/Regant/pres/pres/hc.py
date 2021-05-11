#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import ADS1256#analog to digital
import DAC8532# output pressure
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    DAC = DAC8532.DAC8532()
    ADC.ADS1256_init()
    kpa1 = 4.0 / 1.37
    temp1 = kpa1/20
    kpa2 = 0.0 / 1.37
    temp2 = kpa2/20
    DAC.DAC8532_Out_Voltage(DAC8532.channel_A,  0)
    DAC.DAC8532_Out_Voltage(DAC8532.channel_B,  2.5)
    
    ADC_Value = ADC.ADS1256_GetAll()
    voltage3 = ADC_Value[3]*5.0/0x7fffff
    voltage4 = ADC_Value[4]*5.0/0x7fffff
#        print(voltage)
    print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
    print("press is {} kpa".format((voltage3-0.5)*20/4))
    print("press is {} kpa".format((voltage4-0.5)*20/4))
    print('*'*10)
    time.sleep(1)
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()


