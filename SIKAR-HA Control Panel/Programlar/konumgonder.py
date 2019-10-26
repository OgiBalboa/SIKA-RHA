import tkinter.font
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import RPi.GPIO as GPIO
import os
wait=None
rec=None
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
#PINOUT SETTINGS
## MOTOR 1
GPIO.setup(29,GPIO.OUT) #Pin 3 is set output for servo
pwm=GPIO.PWM(29,50) # creating 50 Hz PWM from Pin 3 (Servo works with 20ms period or 50Hz freq)
pwm.start(0) # Lets start PWM
##MOTOR 2
GPIO.setup(31,GPIO.OUT)
pwm2=GPIO.PWM(31,50)
pwm2.start(0)
##MOTOR 3
GPIO.setup(33,GPIO.OUT)
pwm3=GPIO.PWM(33,50)
pwm3.start(0)

#SERVO SINYAL KODLARI
def SetAngle(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(29, True)   # OUTPUT is high along the duty length
    pwm.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # wait servo to get there
    GPIO.output(29, False)   # OUTPUT is low till starting function again
    pwm.ChangeDutyCycle(0)
    
def SetAngle2(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(31, True)   # OUTPUT is high along the duty length
    pwm2.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # wait servo to get there
    GPIO.output(31, False)   # OUTPUT is low till starting function again
    pwm2.ChangeDutyCycle(0)

def SetAngle3(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(33, True)   # OUTPUT is high along the duty length
    pwm3.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # wait servo to get there
    GPIO.output(33, False)   # OUTPUT is low till starting function again
    pwm3.ChangeDutyCycle(0)
    
#MOTOR ANGLES
def ServoOn():
    x=int(str(angle1.get()))
    y=int(str(angle2.get()))
    if x>180 or y>180:
     messagebox.showerror('TEKİLLİK HATASI', 'Verilebilecek en büyük açı 180 derecedir.')
     return None
    SetAngle(x)
    SetAngle2(y)
    
    
global grp
grp=150
def GrOn():
    global grp
    grp+=1
    SetAngle3(155)
    grinfo=Label(konum,text='Gripper Pozisyonu:'+str(grp)).grid(column=22,row=72)

def GrOff():
    global grp
    grp-=1
    if grp<150 or grp>170:
        messagebox.showerror('TEKİLLİK HATASI','Gripper Konum Sınırlarına ulaşılmıştır.')
        return None
    SetAngle3(176)
    grinfo2=Label(konum,text='Gripper Pozisyonu:'+str(grp)).grid(column=22,row=72)

    
def Gripper():
    z=int(str(gripper.get()))
    SetAngle3(z)
    
    ##Kayit fonk sonu
    
def konumsal():
    global angle1
    global angle2
    global gripper
    global konum
    konum=Tk()
    konum.geometry('900x300')
    konum.title('KONUM BİLGİSİNE GÖRE HAREKET')
    lbl = Label(konum, text="MOTOR 1",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=20, row=0)
    lbl = Label(konum, text="MOTOR 2",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=21, row=0)
    lbl = Label(konum, text="GRIPPER",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=23, row=0)
    angle1 = Entry(konum,width=5)
    angle1.grid(column=20, row=40)
    
    angle2 = Entry(konum,width=5)
    angle2.grid(column=21, row=40)



    btn2= Button(konum,text='Onayla', command=ServoOn,height='2',width='5')
    btn2.grid(column=21,row=41,sticky=W)

    gon= Button(konum,text='Gripper Aç', command=GrOn)
    gon.grid(column=22,row=41)

    goff= Button(konum,text='Gripper Kapat', command=GrOff)
    goff.grid(column=30,row=41,sticky=W)
    gripper=Scale(konum,from_=150,to=180,orient=HORIZONTAL)
    gripper.grid(column=23,row=100)

    grpbutton=Button(konum,text='Move',command=Gripper)
    grpbutton.grid(column=23,row=181)
    konum.mainloop()
konumsal()
