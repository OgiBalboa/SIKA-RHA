#RASPI PINOUT

from tkinter import *
import os

def kill():
	#os.chdir('..')
	raspi.destroy()
raspi = Tk()
raspi.title(" RASPI PINOUT ")
raspi.geometry("1000x600")
reso = PhotoImage(file="raspipinout.png")
Label(raspi, image = reso).grid(column = 1,row = 0)

Button(raspi,text=" Cikis " , command = kill).grid(column = 1,row = 1)
raspi.mainloop()
