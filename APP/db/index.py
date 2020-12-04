import pymysql
from sql import *

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",password="chuangli",
    database="autocell",
    charset="utf8")
cur = mydb.cursor()

def findUser(userName):
    cur.execute(searchUser,[userName])
    result = cur.fetchall()
    return result
def addUsers(userName,passWord):
    cur.execute(addUser,[userName,passWord])
    mydb.commit()
    







