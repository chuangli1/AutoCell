from time import time
import threading
import cv2
def gen(camera):
    camera.start()
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')
  
class Camera(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.cap = cv2.VideoCapture(0)
  def get_frame(self):
      ret,frame = self.cap.read()
      ret,frame = cv2.imencode('.jpg', frame)
      return frame