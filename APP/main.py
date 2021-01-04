#main
from flask import Flask,render_template,request,jsonify,Response,send_from_directory
from flask_cors import CORS
import sys  
sys.path.append('./db')
import os
from db.index import *
import time #主要是用于处理Flask不适用于生产环境的原因
from imaging.camera import gen, Camera,genVideo
camera = Camera()
camera.start()


managerName = 'chuangli'
app = Flask(__name__, 
           template_folder= "../Web_UI/dist",
           static_folder= "../Web_UI/dist",
           static_url_path='')
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)

#登录相关
@app.route('/')
def hello_world():
   return render_template( 'index.html')

#用户账户相关
@app.route('/deleteUser',methods=['POST'])
def deleteUser_m():
   userName = request.form['username']
   passWord = request.form['password']
   re =  findUser(userName)
   if re:
      pwd = findUser(userName)[0][2]
      if(passWord==pwd):
         deleteUsers(userName)
         return jsonify({'code':1})
      else:
         return jsonify({'code':2})   
   else:
      return jsonify({'code':0})     
@app.route('/addUser',methods=['POST'])
def addUser_m():
   userName = request.form['username']
   passWord = request.form['password']
   try:
      re =  findUser(userName)
      if re:
         return jsonify({'code':0})
      addUsers(userName,passWord)
      return jsonify({'code':1})
   except:
      return jsonify({'code':2})
@app.route('/login',methods=['POST'])
def login():
   userName = request.form['username']
   passWord = request.form['password']
   re =  findUser(userName)
   if re:
      pwd = findUser(userName)[0][2]
      if(passWord==pwd):
         if userName == managerName:
             return jsonify({'code':3})   
         else:
             return jsonify({'code':1})
      else: return jsonify({'code':2})
   else:
      return jsonify({'code':0})
@app.route('/loadTeam',methods=['GET'])
def loadTeam():
   try:
      time.sleep(0.5)
      re =  searchAllUsers()
      return jsonify({'code':1,'members':re})
   except:
      return jsonify({'code':0})
@app.route('/updateUser',methods=['POST'])
def updateUser():
   userID = request.form['user_id']
   passWord = request.form['user_password']
   email = request.form['user_mail']
   phone = request.form['user_phone']
   address = request.form['user_address']
   office = request.form['user_office']
   try:
       updateUsers(email,phone,office,address,passWord,userID)
       return jsonify({'code':1})
   except:
      return jsonify({'code':0})



#视频传输相关
@app.route('/video',methods=['GET'])
def video():
    return Response(gen(camera),
          mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/videoPlay',methods=['GET'])
def videoPlay():
    videoName = request.args.get('video_name')
    return Response(genVideo(videoName),
          mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/videoRecordStart',methods=['POST'])
def videoRecordStart():
    videoName = request.form['videoName']
    if os.path.exists('./video/'+videoName+'.avi'):
         videoName = videoName+'(1)'
    try:
      camera.start_c(videoName,-1)
      return jsonify({'code':1})
    except:
      return jsonify({'code':0})
@app.route('/videoRecordStop',methods=['POST'])
def videoRecordStop():
    try:
      camera.stop_c()
      return jsonify({'code':1})
    except:
      return jsonify({'code':0})
@app.route('/videoRecordSave',methods=['POST'])
def videoRecordSave():
    userName = request.form['userName']
    videoName = request.form['videoName']
    videoDate = request.form['videoDate']
    if os.path.exists('./video/'+videoName+'(1).avi'):
         videoName = videoName+'(1)'
         
    try:
      addVideos(userName,videoName,videoDate)
      return jsonify({'code':1})
    except:
      return jsonify({'code':0})
@app.route('/videoGet',methods=['GET'])
def videoGet():
   userName = request.args.get('user_name')
   try:
      videoList =  searchVideos(userName)
      return jsonify({'code':1,'videoList':videoList})
   except:
      return jsonify({'code':0})
@app.route('/videoGetAll',methods=['GET'])
def videoGetAll():
   try:
      time.sleep(0.4)
      videoList =  searchAllVideos()
      return jsonify({'code':1,'videoList':videoList})
   except:
      return jsonify({'code':0})
@app.route('/videoDownload',methods=['GET'])
def videoDownload():
   videoName = request.args.get('video_name')
   return send_from_directory('./video',filename=videoName,as_attachment=True)
@app.route('/videoDelete',methods=['POST'])
def videoRemove():
    videoID = request.form['video_id']
    try:
       deleteVideos(videoID)
       return jsonify({'code':1})
    except:
       return jsonify({'code':0})
   
#留言板相关
@app.route('/addInfo',methods=['POST'])
def addInfo():
   info_user = request.form['info_user']
   info_content = request.form['info_content']
   info_date = request.form['info_date']
   try:
      addInfos(info_user,info_content,info_date)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/deleteInfo',methods=['POST'])
def deleteInfo():
   info_id = request.form['info_id']
   try:
      deleteInfos(info_id)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/deleteAllInfo',methods=['POST'])
def deleteAllInfo():
   try:
      deleteAllInfos()
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/loadInfos',methods=['GET'])
def loadInfo():
   try:
      time.sleep(0.1)
      re = findInfos()
      return jsonify({'code':1,'infos':re})
   except:
      return jsonify({'code':0})

#任务相关
@app.route('/addTask',methods=['POST'])
def addTask():
   taskType = request.form['type']
   taskName = request.form['task_name']
   taskUser = request.form['task_username']
   taskTime = request.form['task_time']
   taskInterval = request.form['task_interval']
   taskDate= request.form['task_date']
   try:
      time.sleep(0.3)
      if(taskType=='regant'):
         taskValve = request.form['task_valve']
         taskPres = request.form['task_pres']
         addRegantTasks(taskName,taskUser,taskDate,taskValve,taskPres,taskTime,taskInterval)
      else:
         addMonitorTasks(taskName,taskUser,taskDate,taskTime,taskInterval)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/deleteTask',methods=['POST'])
def deleteTask():
   taskType = request.form['type'] 
   taskID = request.form['task_id']
   try:
      if(taskType=='regant'):
         deleteRegantTasks(taskID)
      else:
         deleteMonitorTasks(taskID)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/updateTask',methods=['POST'])
def updateTask():
   taskType = request.form['type']
   taskName = request.form['task_name']
   taskUser = request.form['task_username']
   taskTime = request.form['task_time']
   taskInterval = request.form['task_interval']
   taskDate= request.form['task_date']
   taskID = request.form['task_id']
   try:
      if(taskType=='regant'):
         taskValve = request.form['task_valve']
         taskPres = request.form['task_pres']
         updateRegantTasks(taskName,taskUser,taskDate,taskValve,taskPres,taskTime,taskInterval,taskID)
      else:
         print(taskName,taskUser,taskDate,taskTime,taskInterval,taskID)
         updateMonitorTasks(taskName,taskUser,taskDate,taskTime,taskInterval,taskID)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/loadTasks',methods=['GET'])
def loadTasks():
   taskType = request.args.get('type')
   try:
      if(taskType=='regant'):
         re = searchRegantTasks()
         return jsonify({'code':1,'tasks':re})
      else:
         re1 = searchMonitorTasks()
         return jsonify({'code':1,'tasks':re1})
   except:
      return jsonify({'code':0})
#正在执行的任务
@app.route('/addTaskList',methods=['POST'])
def addTaskList():
   taskType = request.form['type']
   taskId = request.form['task_id']
   listDate= request.form['list_date']
   try:
      addTaskLists(taskType,taskId,listDate)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})
@app.route('/loadTaskList',methods=['GET'])
def loadTaskList():
   try:
      re = searchTasklists()
      return jsonify({'code':1,'taskList':re})
   except:
      return jsonify({'code':0})
@app.route('/deleteTaskList',methods=['POST'])
def deleteTaskList():
   taskId = request.form['task_id']
   taskType = request.form['task_type']
   try:
      deleteTaskLists(taskId,taskType)
      return jsonify({'code':1})
   except:
      return jsonify({'code':0})


if __name__ == '__main__':
   app.run(threaded=True)