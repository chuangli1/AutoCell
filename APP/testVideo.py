from flask import url_for,redirect, session,Flask,render_template,request,jsonify,Response,send_from_directory
from flask_cors import CORS
import cv2
import sys
sys.path.append('./db')
from db.index import *
import time #主要是用于处理Flask不适用于生产环境的原因
managerName = 'chuangli'
app = Flask(__name__, 
           template_folder= "../Web_UI/dist",
           static_folder= "../Web_UI/dist",
           static_url_path='')
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)
app.secret_key = '!@#$%^&*()11chuangli'
camera = cv2.VideoCapture(0);
def gen(camera):
    while True:
        _,frame = camera.read();
        ret, frame = cv2.imencode('.jpg', frame)
        try:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')
        except:
            break
#视频传输相关
@app.route('/video',methods=['GET'])
def video():
    return Response(gen(camera),
          mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/login',methods=['POST'])
def login():

    return jsonify({'code':1})

if __name__ == '__main__':
   camera = cv2.VideoCapture(0);
   
   app.run(threaded=True,port=5000)