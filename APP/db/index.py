import pymysql
from .sql import *

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",password="chuangli",
    database="autocell",
    charset="utf8")
cur = mydb.cursor()

#user
def findUser(userName):
    mydb.ping(reconnect=True)
    cur.execute(searchUser,[userName])
    result = cur.fetchall()
    return result
def addUsers(userName,passWord):
    mydb.ping(reconnect=True)
    cur.execute(addUser,[userName,passWord])
    mydb.commit()
def deleteUsers(userName):
    mydb.ping(reconnect=True)
    cur.execute(deleteUser,[userName])
    mydb.commit()
def searchAllUsers():
    mydb.ping(reconnect=True)
    cur.execute(searchAlluser)
    result = cur.fetchall()
    return result
def updateUsers(user_mail,user_phone,user_office,user_addres,user_password,user_id):
    mydb.ping(reconnect=True)
    if(user_password==''):
        cur.execute(updateUser1,[user_mail,user_phone,user_office,user_addres,user_id])
    else:
        cur.execute(updateUser,[user_mail,user_phone,user_office,user_addres,user_password,user_id])
    mydb.commit()



#info
def addInfos(info_user,info_content,info_date):
    mydb.ping(reconnect=True)
    cur.execute(addInfo,[info_user,info_content,info_date])
    mydb.commit()
def deleteInfos(info_id):
    mydb.ping(reconnect=True)
    cur.execute(deleteInfo,[info_id])
    mydb.commit()
def deleteAllInfos():
    mydb.ping(reconnect=True)
    cur.execute(deleteAllInfo)
    mydb.commit()
def findInfos():
    mydb.ping(reconnect=True)
    cur.execute(searchInfo)
    result = cur.fetchall()
    return result

#video
def addVideos(user_name, video_name, video_date):
    mydb.ping(reconnect=True)
    cur.execute(addVideo,[user_name,video_name,video_date])
    mydb.commit()
def searchAllVideos():
    mydb.ping(reconnect=True)
    cur.execute(searchAllVideo)
    result = cur.fetchall()
    return result
def searchVideos(user_name):
    mydb.ping(reconnect=True)
    cur.execute(searchVideo,[user_name])
    result = cur.fetchall()
    return result
def deleteVideos(video_id):
    mydb.ping(reconnect=True)
    cur.execute(deleteVideo,[video_id])
    mydb.commit()

#task
def addRegantTasks(task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval):
    mydb.ping(reconnect=True)
    cur.execute(addRegantTask,[task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval])
    mydb.commit()
def searchRegantTasks():
    mydb.ping(reconnect=True)
    cur.execute(searchRegantTask)
    result = cur.fetchall()
    return result
def findRegantTasks(task_id):
    mydb.ping(reconnect=True)
    cur.execute(findRegantTask,[task_id])
    result = cur.fetchall()
    return result
def deleteRegantTasks(task_id):
    mydb.ping(reconnect=True)
    cur.execute(deleteRegantTask,[task_id])
    mydb.commit()
def updateRegantTasks(task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval,task_id):
    cur.execute(updateRegantTask,[task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval,task_id])
    mydb.commit()

def addMonitorTasks(task_name,task_username,task_date,task_time,task_interval,task_location):
    mydb.ping(reconnect=True)
    cur.execute(addMonitorTask,[task_name,task_username,task_date,task_time,task_interval,task_location])
    mydb.commit()
def searchMonitorTasks():
    mydb.ping(reconnect=True)
    cur.execute(searchMonitorTask)
    result = cur.fetchall()
    return result
def findMonitorTasks(task_id):
    mydb.ping(reconnect=True)
    cur.execute(findMonitorTask,[task_id])
    result = cur.fetchall()
    return result
def deleteMonitorTasks(task_id):
    mydb.ping(reconnect=True)
    cur.execute(deleteMonitorTask,[task_id])
    mydb.commit()
def updateMonitorTasks(task_name,task_username,task_date,task_time,task_interval,task_location,task_id):
    mydb.ping(reconnect=True)
    cur.execute(updateMonitorTask,[task_name,task_username,task_date,task_time,task_interval,task_location,task_id])
    mydb.commit()

#ontasklist
def addTaskLists(task_type,task_id,list_date):
    mydb.ping(reconnect=True)
    cur.execute(addTaskList,[task_type,task_id,list_date])
    mydb.commit()
def searchTasklists():
    mydb.ping(reconnect=True)
    cur.execute(searchTaskList)
    result = cur.fetchall()
    return result
def deleteTaskLists(task_id,task_type):
    mydb.ping(reconnect=True)
    cur.execute(deleteTaskList,[task_id,task_type])
    mydb.commit()

#location
def addLocations(user,name,angle,line):
    mydb.ping(reconnect=True)
    cur.execute(addLocation,[user,name,angle,line])
    mydb.commit()
def searchLocations(user):
    mydb.ping(reconnect=True)
    cur.execute(searchLocation,[user])
    result = cur.fetchall()
    return result
def deleteLocations(id,user):
    mydb.ping(reconnect=True)
    cur.execute(deleteLocation,[id,user])
    mydb.commit()
def findLocations(id,user):
    mydb.ping(reconnect=True)
    cur.execute(findLocation,[id,user])
    result = cur.fetchall()
    return result
def updateLocations(angle,line,id,user):
    mydb.ping(reconnect=True)
    cur.execute(updateLocation,[angle,line,id,user])
    mydb.commit()






