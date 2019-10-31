#-------------------------------------------------------------------------------
# Name:        Control Panel    
# Purpose:     SIKA-RHA Robot Kontrol GUI
#
# Author:      @ogibalboa
#
# Created:     07.10.2018
# Copyright:   (c) OgiBalboa 2019
# Licence:     <GNU GCC>
#-------------------------------------------------------------------------------

import webbrowser
import tkinter.font
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import RPi.GPIO as GPIO
import os
from multiprocessing import Process
from threading import Thread
from ogibalboa import resim
wait=None
rec=None
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
def konumsal():
    def calistir():
        os.chdir('Programlar')
        os.system('python3 konumgonder.py')
        os.chdir("..")
    dal = Thread(target = calistir)
    dal.start()    

def kayit():
    def calistir():
        os.chdir('Programlar')
        os.system('python3 entrykayit.py')
        os.chdir("..")
    dal = Thread(target = calistir)
    dal.start()    
def slider():
    def calistir():
        os.chdir('Programlar')
        os.system('python3 slider.py')
        os.chdir("..")
    dal = Thread(target = calistir)
    dal.start()     
def serkayit():
    def calistir():
        os.chdir('Programlar')
        os.system('python3 ser_konum_kayit.py')
        os.chdir("..")
    dal = Thread(target = calistir)
    dal.start()    
def github():
    onay=messagebox.askokcancel('Yönlendirme', 'SIKARHA! Github sayfasına yönlendiriliyorsunuz. Onay ?')
    if onay == True:
         webbrowser.open('https://github.com/OgiBalboa/servo')
    else:
        return None
def test():
    os.chdir('test')
    os.system('nano test.ino')
    os.chdir("..")

def raspipinout():
    print("fonksiyona girildi")
    def calistir():
        try:
            os.chdir('help')
            os.system('python3 raspi.py')
        except:
            print("Dosya açma hatası")
        finally :
            os.chdir("..")
        
    dal = Thread(target = calistir)
    dal.start()  
    #os.chdir("..")
def donothing():
    messagebox.showinfo('BİLGİ','SEKME ŞU ANDA BOŞ. YAKINDA İÇERİK EKLENECEK')

pencere = Tk()
#--------------------RESİMLERİ YÜKLE ----------------------------
try:
    record = resim("Programlar/pics/records.png")
    roboticon = resim("Programlar/pics/roboticon.png")
    settings = resim("Programlar/pics/settings.png")
    kalibrate = resim("Programlar/pics/kalibrate.png")
    worldkor = resim("Programlar/pics/worldkor.png")
    toolkor = resim("Programlar/pics/toolkor.png")
    basekor = resim("Programlar/pics/basekor.png")
except:
    print("HATA ! Resimler Yüklenemedi...")
##Menu Toolbar
menubar = Menu(pencere)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Yeni", command=test)
filemenu.add_command(label="Aç", command=donothing)
filemenu.add_command(label="Kaydet", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Çık", command=pencere.destroy)
menubar.add_cascade(label="Dosya", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Konum Bilgisi", command=konumsal)
editmenu.add_command(label="Slider", command=slider)
editmenu.add_command(label="Pot ile", command=donothing)

kayitmenu= Menu(menubar, tearoff=0)
kayitmenu.add_command(label="Hareket Kaydet",command=kayit)
menubar.add_cascade(label="Kayit",menu=kayitmenu)
menubar.add_cascade(label="Hareket", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Raspberry Pinleri", command=raspipinout)
helpmenu.add_command(label="Hakkında", command=donothing)
menubar.add_cascade(label="Yardım", menu=helpmenu)


#Başlık
pencere.title("SIKA-RHA Control Panel")
pencere.geometry('1920x780')
#pencere.configure(background = "#00004d")
pencere.attributes("-fullscreen",False)
lbl = Label(pencere, text="  SIKA-RHA! CONTROL PANEL  ",fg='orange',bg='#00004d' \
,font=("Algerian",24)).place(x=700,y=0)
#-----------------------------SOL PANEL--------------------------------------------------------
Label(pencere, text="Robot Kontrol",font=("Algerian",12)).place(x=40,y=230)
Button(pencere,image = roboticon.render,command = donothing,bg="#00004d").place(x = 0,y = 30)
serial = Button(pencere,image = record.render,command = serkayit,bg="#00004d").place(x = 370,y = 30)
Label(pencere, text="Konum Kayıt",font=("Algerian",12)).place(x=400,y=230)
infobtn=Button(pencere,text='GITHUB SAYFASI',fg='yellow',bg="#00004d",font=("Arial",16),command=github)\
.place(x = 10 , y = 900)
Button(pencere,text='ÇIKIŞ',fg='red',bg="#00004d",font=("Arial",16),command=pencere.destroy)\
.place(x = 850 , y = 900)
#----------------------------sağ panel----------------------------------------
Button(pencere,image = kalibrate.render,command = donothing, bg="#00004d").place(x = 1350, y = 30)
Label(pencere,text = " Kalibrasyon ",font=('Algerian',12)).place(x = 1390, y = 230  )
Button(pencere,image = settings.render,command = donothing, bg="#00004d").place(x = 1720,y = 30)
Label(pencere,text = " Ayarlar ",font=('Algerian',12)).place(x = 1780, y = 230  )
#--------------------------KONFİGÜRASYONLAR -----------------------------------------------------
Label(pencere, text="Robot Konfigürasyonları",font=("Arial",20),fg = "brown").place(x=800,y=50)
speed = Scale(pencere,from_=0,to=100,orient=HORIZONTAL).place(x = 900,y = 90)
Label(pencere,text = "Hareket hızı  (%)",font=("Arial",10),fg = "#00004d").place( x = 750, y = 105)
Button(pencere,text = "OK",command = donothing,font=("Arial",12),fg = "#00004d").place( x = 1080, y = 105)
Label(pencere,text = "Hareket Koordinat Seçimi",font=("Arial",14),fg = "#00004d").place( x = 850, y = 140)

Button(pencere,image = basekor.render,command = donothing).place(x = 750, y = 180)
Label(pencere,text = "Robot Base Orjinli Koordinat",font=("Arial",10),fg = "#00004d").place( x = 700, y = 250)
Button(pencere,image = toolkor.render,command = donothing).place(x = 950, y = 180)
Label(pencere,text = "Tool Orijinli Koordinat",font=("Arial",10),fg = "#00004d").place( x = 900, y = 250)
Button(pencere,image = worldkor.render,command = donothing).place(x = 1110, y = 180)
Label(pencere,text = "Ana Koordinat Sistemi",font=("Arial",10),fg = "#00004d").place( x = 1060, y = 250)

pencere.config(menu=menubar)


pencere.mainloop()




