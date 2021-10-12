from .sensors import ccs811,hdc1080
from apscheduler.schedulers.background import BackgroundScheduler
from db.index import addInfos,addVideos
from  openpyxl import  Workbook
import time
def genSensors():
    CO2,TVOC = ccs811.readCO2()
    TEMP, HUMI = hdc1080.readTemp()
    return [round(CO2,2),round(TVOC,2),round(TEMP,2),round(HUMI,2)]
def recordSensors():
    scheduler = BackgroundScheduler()
    warningN = [0,0,0]
    workbook = [0,0]
    scheduler.add_job(record(), 'interval', minutes=3, start_date =time.localtime(), end_date=times[1], id=str(taskId),args=[warningN,workbook])

def record(warningN,workbook):
    if(warningN[0]%480==0):#每天的数据保存到一个新文件里
        workbook.pop()
        workbook.pop()
        workbook.append(Workbook())
        workbook.append(workbook[0].active)
        workbook[1].append(['时间','二氧化碳','温度','湿度'])
        workbook[0].save('./video/传感器数据记录表%s.xlsx'%(int(warningN[0]/480))) #一个新文件
        warningN[0] = warningN[0]+1
        addVideos('系统','传感器数据记录表%s.xlsx'%(warningN[0]%480),time.strftime('%Y/%m/%d %H:%M',time.localtime()))
    data = genSensors()
    if data[0]>1000 or data[2]>38 or data[3]>80 or data[0]<300 or data[2]<36 or data[3]<20:
        warningN[1] = warningN[1]+1
        warningN[2] = 0
        if(warningN[1]>5): #短时间内出现5次以上异常数据，记录
            addInfos('系统：环境数据异常！！！',"CO2: %s; \n 温度：%s; \n 湿度：%s。"%(data[0],data[2],data[3]),time.strftime('%Y/%m/%d %H:%M:%S',time.localtime()))    
            warningN[1] = 0
    else:
        warningN[1] = warningN[1]-1
        warningN[2] = warningN[2]+1
        if(warningN[2]>10): #连续10次监测数据正常，异常情况排除
            warningN[1] = 0
    workbook[1].append(time.strftime('%Y/%m/%d %H:%M',time.localtime()),data[0],data[2],data[3]]) # 不带样式的写入
    if(warningN[0]%5==0):#每15分钟保存一次数据
        workbook.save('./video/传感器数据记录表%s.xlsx'%(int(warningN[0]/480))) # 保存文件
    warningN[0] = warningN[0]+1
    
    


