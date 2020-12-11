
addUser = 'insert into user (user_name,user_password) values(%s,%s);'
deleteUser = "delete from user where user_name=%s;"
searchUser = 'select * from user where user_name=%s;'

addInfo = 'insert into info (info_user,info_content,info_date) values(%s,%s,%s);'
searchInfo = 'select * from info;'
deleteInfo = "delete from info where info_id=%s;"
deleteAllInfo = "delete * from info;"

addVideo = 'insert into video (user_name,video_name,video_date) values(%s,%s,%s);'
deleteVideo = "delete from video where video_id=%s;"
searchVideo = 'select * from video where user_name=%s;'
searchAllVideo = 'select * from video'

