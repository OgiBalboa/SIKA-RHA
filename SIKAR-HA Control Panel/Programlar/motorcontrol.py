import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
class Motor:
  def __init__(self,mnum):
    self.mnum  = mnum
    self.cout = 0
  def setup(self):
    GPIO.setup(self.mnum,GPIO.OUT)
    self.pwm = GPIO.PWM(self.mnum,50)
    self.pwm.start(0)
  def stop(self):
    self.pwm.stop()

  def SetAngle(self,angle):  
    self.duty = angle / 18 + 2      
  def run(self,ang):
    for self.cout in range (0,ang):
      self.SetAngle(ang)
      time.sleep(0.005)
      self.cout +=1

    if self.cout == ang:
      self.cout =0
     
Testy = Motor(12)
Testy.setup()
while 1:
  x = int(input("ACIII"))
  Testy.run(x)
