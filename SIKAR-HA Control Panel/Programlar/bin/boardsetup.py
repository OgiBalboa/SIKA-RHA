"""
raspı pın setup

author = @ogibalboa

"""
import RPi.GPIO as pin
import os
import time
import tkinter
from tkinter import *
from tkinter import Scale
class raspiservo():
    def __init__(self,):
        pin.setwarnings(False)
        pin.setmode(pin.BOARD)
        #MOTOR 1

        pin.setup(29,pin.OUT)
        self.pwm=pin.PWM(29,50) 
        self.pwm.start(5) # Lets start PWM
        
        ##MOTOR 2
        pin.setup(31,pin.OUT)
        self.pwm2=pin.PWM(31,50)
        self.pwm2.start(5)
        
        ##MOTOR 3
        pin.setup(33,pin.OUT)
        self.pwm3=pin.PWM(33,50)
        self.pwm3.start(5)
    
    def motor(self,motorno,angle):
        self.duty = angle/18 + 2
        self.motorinfo(motorno)
        pin.output(self.pinno,True)
        self.pwmno.ChangeDutyCycle(self.duty)
        time.sleep(0.2)
        #pin.output(self.pinno, False)   # OUTPUT is low till starting function again
        ##self.pwmno.ChangeDutyCycle(0)
        
    def motorinfo(self,motorno):
        if motorno == 1:
            self.pinno = 29
            self.pwmno = self.pwm
        elif motorno == 2:
            self.pinno = 31
            self.pwmno = self.pwm2
        elif motorno ==3:
            self.pinno = 33
            self.pwmno = self.pwm3
        else :
            self.pinno = 1
            self.pwmno = self.pwm1

new = raspiservo()
root = tkinter.Tk()
def goo(angle):
    #aci = int(str(angle.get()))
    new.motor(1,int(angle))
angle = Scale(root, from_ = 0, to = 180,orient = HORIZONTAL,command = goo)
angle.pack()
new.motor(3,int(str(angle.get())))
root.mainloop()
