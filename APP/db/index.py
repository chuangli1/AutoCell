import pymysql
from sql import *

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",password="chuangli",
    database="autocell",
    charset="utf8")
cur = mydb.cursor()

#user
def findUser(userName):
    cur.execute(searchUser,[userName])
    result = cur.fetchall()
    return result
def addUsers(userName,passWord):
    cur.execute(addUser,[userName,passWord])
    mydb.commit()
def deleteUsers(userName):
    cur.execute(deleteUser,[userName])
    mydb.commit()

#info
def addInfos(info_user,info_content,info_date):
    cur.execute(addInfo,[info_user,info_content,info_date])
    mydb.commit()
def deleteInfos(info_id):
    cur.execute(deleteInfo,[info_id])
    mydb.commit()
def deleteAllInfos():
    cur.execute(deleteAllInfo)
    mydb.commit()
def findInfos():
    cur.execute(searchInfo)
    result = cur.fetchall()
    return result

#video
def addVideos(user_name, video_name, video_date):
    cur.execute(addVideo,[user_name,video_name,video_date])
    mydb.commit()
def searchAllVideos():
    cur.execute(searchAllVideo)
    result = cur.fetchall()
    return result
def searchVideos(user_name):
    cur.execute(searchVideo,[user_name])
    result = cur.fetchall()
    return result
def deleteVideos(video_id):
    cur.execute(deleteVideo,[video_id])
    mydb.commit()

#task
def addRegantTasks(task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval):
    cur.execute(addRegantTask,[task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval])
    mydb.commit()
def searchRegantTasks():
    cur.execute(searchRegantTask)
    result = cur.fetchall()
    return result
def deleteRegantTasks(task_id):
    cur.execute(deleteRegantTask,[task_id])
    mydb.commit()
def updateRegantTasks(task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval,task_id):
    cur.execute(updateRegantTask,[task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval,task_id])
    mydb.commit()

def addMonitorTasks(task_name,task_username,task_date,task_time,task_interval):
    cur.execute(addMonitorTask,[task_name,task_username,task_date,task_time,task_interval])
    mydb.commit()
def searchMonitorTasks():
    cur.execute(searchMonitorTask)
    result = cur.fetchall()
    return result
def deleteMonitorTasks(task_id):
    cur.execute(deleteMonitorTask,[task_id])
    mydb.commit()
def updateMonitorTasks(task_name,task_username,task_date,task_time,task_interval,task_id):
    cur.execute(updateMonitorTask,[task_name,task_username,task_date,task_time,task_interval,task_id])
    mydb.commit()







