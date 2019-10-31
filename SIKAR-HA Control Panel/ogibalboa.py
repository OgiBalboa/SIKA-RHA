"""

author : @ogibalboa
date : 20.10.2019
"""
#-------------------------------------------------------------------------------
# Name:        ogibalboa
# Purpose:     S-HA PANEL geliştirmeleri için oluşturulmuş modül.
#
# Author:      @ogibalboa
#
# Created:     07.10.2019
# Copyright:   (c) OgiBalboa 2019
# Licence:     <GNU GCC>
#-------------------------------------------------------------------------------
#----------------------------RESİM YÜKLEME FONKSİYONU---------------
from PIL import Image,ImageTk
class resim():
    def __init__(self,path):
        self.pic = Image.open(str(path))  
        self.render = ImageTk.PhotoImage(self.pic)
