from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
import sys  
sys.path.append('./db') 
from db.index import *
managerName = 'chuangli'
app = Flask(__name__, 
           template_folder= "../Web_UI/dist",
           static_folder= "../Web_UI/dist",
           static_url_path='')
cors = CORS(app)

@app.route('/')
def hello_world():
   return render_template( 'index.html')
   
@app.route('/get',methods=['GET'])
def hello():
   return 'HELLO'
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
      

if __name__ == '__main__':
   app.run()