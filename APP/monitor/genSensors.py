from .sensors import ccs811,hdc1080
from apscheduler.schedulers.background import BackgroundScheduler
from db.index import addInfos,addVideos
import xlwt
import time
n = 0 #异常次数
g = 0 #正常次数
s = 0 #总次数
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
workbook.save('./video/传感器数据记录表0.xls') # 保存文件
addVideos('系统','传感器数据记录表0.xls',time.strftime('%Y/%m/%d %H:%M',time.localtime()))
def genSensors():
    CO2,TVOC = ccs811.readCO2()
    TEMP, HUMI = hdc1080.readTemp()
    return [CO2,TVOC,TEMP,HUMI]
def recordSensors():
    scheduler = BackgroundScheduler()
    warningN = [0,0,0]
    scheduler.add_job(record(), 'interval', minutes=3, start_date =time.localtime(), end_date=times[1], id=str(taskId),args=[warningN])

def record():
    s = s+1
    data = genSensors()
    if data[0]>1000 or data[2]>38 or data[3]>80 or data[0]<300 or data[2]<36 or data[3]<20:
        n = n+1
        g = 0
        if(n>5): #短时间内出现5次以上异常数据，记录
            addInfos('系统：环境数据异常！！！',"CO2: %s; 温度：%s; 湿度：%s。"%(data[0],data[2],data[3]),time.strftime('%Y/%m/%d %H:%M:%S',time.localtime()))    
            n = 0
    else:
        n = n-1
        g = g+1
        if(g>10): #连续10次监测数据正常，异常情况排除
            n = 0
    worksheet.write(s, 0, time.strftime('%Y/%m/%d %H:%M',time.localtime())) # 不带样式的写入
    worksheet.write(s, 1, data[0]) # 不带样式的写入
    worksheet.write(s, 2, data[2]) # 不带样式的写入
    worksheet.write(s, 3, data[3]) # 不带样式的写入
    if(s%5==0):#每15分钟保存一次数据
        workbook.save('formatting.xls') # 保存文件
    if(s%480==0):#每天的数据保存到一个新文件里
        workbook = xlwt.Workbook(encoding = 'ascii')
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0, 0,'时间') # 不带样式的写入
        worksheet.write(0, 1, '二氧化碳') # 不带样式的写入
        worksheet.write(0, 2, '温度') # 不带样式的写入
        worksheet.write(0, 3, '湿度') # 不带样式的写入
        workbook.save('./video/传感器数据记录表%s.xls'%(s%480)) #一个新文件
        addVideos('系统','传感器数据记录表%s.xls'%(s%480),time.strftime('%Y/%m/%d %H:%M',time.localtime()))
    


