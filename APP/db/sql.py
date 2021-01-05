
addUser = 'insert into user (user_name,user_password,user_mail,user_phone,user_office,user_address,level) values(%s,%s,"","","","",1);'
deleteUser = "delete from user where user_name=%s;"
searchUser = 'select * from user where user_name=%s;'
searchAlluser = 'select user_name,user_mail,user_phone,user_office,user_address,level,user_id from user;'
updateUser = 'update user set user_mail=%s,user_phone=%s,user_office=%s,user_address=%s,user_password=%s where user_id=%s;'
updateUser1 = 'update user set user_mail=%s,user_phone=%s,user_office=%s,user_address=%s where user_id=%s;'

addInfo = 'insert into info (info_user,info_content,info_date) values(%s,%s,%s);'
searchInfo = 'select * from info;'
deleteInfo = "delete from info where info_id=%s;"
deleteAllInfo = "delete * from info;"

addVideo = 'insert into video (user_name,video_name,video_date) values(%s,%s,%s);'
deleteVideo = "delete from video where video_id=%s;"
searchVideo = 'select * from video where user_name=%s;'
searchAllVideo = 'select * from video;'

addRegantTask = 'insert into regants (task_name,task_username,task_date,task_valve,task_pres,task_time,task_interval) values(%s,%s,%s,%s,%s,%s,%s);'
deleteRegantTask = "delete from regants where task_id=%s;"
searchRegantTask = 'select * from regants;'
findRegantTask = 'select * from regants where task_id=%s;'
updateRegantTask = 'update regants set task_name=%s,task_username=%s,task_date=%s,task_valve=%s,task_pres=%s,task_time=%s,task_interval=%s where task_id=%s'

addMonitorTask = 'insert into monitor (task_name,task_username,task_date,task_time,task_interval) values(%s,%s,%s,%s,%s);'
deleteMonitorTask = "delete from monitor where task_id=%s;"
findMonitorTask = "select * from monitor where task_id=%s;"
searchMonitorTask = 'select * from monitor;'
updateMonitorTask = 'update monitor set task_name=%s,task_username=%s,task_date=%s,task_time=%s,task_interval=%s where task_id=%s'

addTaskList = 'insert into tasklist (task_type,task_id,list_date) values(%s,%s,%s);'
deleteTaskList = "delete from tasklist where task_id=%s and task_type=%s;"
searchTaskList = 'select * from tasklist;'