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
    mydb.commit()
def searchVideos(user_name):
    cur.execute(searchVideo,[user_name])
    result = cur.fetchall()
    return result
def deleteVideos(video_id):
    cur.execute(deleteVideo,[video_id])
    mydb.commit()







