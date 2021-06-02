import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",password="chuangli",
    database="autocell",
    charset="utf8")
cur = mydb.cursor()
creatLoction = " CREATE TABLE IF NOT EXISTS `locationlist`(\
                    `location_id` INT UNSIGNED AUTO_INCREMENT,\
                    `location_name` VARCHAR(100) NOT NULL,\
                    `user_name` VARCHAR(100) NOT NULL,\
                    `location_angle` INT,\
                    `location_line` INT,\
                    PRIMARY KEY ( `location_id` )\
                    )ENGINE=InnoDB DEFAULT CHARSET=utf8;"
def creatTable(name):
    mydb.ping(reconnect=True)
    cur.execute(name)
    mydb.commit()
creatTable(creatLoction)
     
