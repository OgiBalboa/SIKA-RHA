"""
S-HA PANEL gekiştirmeleri için oluşturulmuş modül.
author : @ogibalboa
date : 20.10.2019
"""
#----------------------------RESİM YÜKLEME FONKSİYONU---------------
from PIL import Image,ImageTk
class resim():
    def __init__(self,path):
        self.pic = Image.open(str(path))  
        self.render = ImageTk.PhotoImage(self.pic)
