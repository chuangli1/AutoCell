
addUser = 'insert into user (user_name,user_password) values(%s,%s);'
deleteUser = "delete from user where user_name=%s;"
searchUser = 'select * from user where user_name=%s;'

addInfo = 'insert into info (info_user,info_content,info_date) values(%s,%s,%s);'
searchInfo = 'select * from info;'
deleteInfo = "delete from info where info_id=%s;"
deleteAllInfo = "delete * from info;"
