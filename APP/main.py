from flask import Flask,render_template

from flask_cors import CORS
app = Flask(__name__,
           template_folder= "../Web_UI/dist",
           static_folder= "../Web_UI/dist",
           static_url_path='')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def hello_world():
   return render_template( 'index.html')

if __name__ == '__main__':
   app.run()