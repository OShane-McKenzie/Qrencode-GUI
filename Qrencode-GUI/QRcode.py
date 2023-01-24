import os, sys
from sys import platform
from os.path import exists

from PyQt5.QtWidgets import QFileDialog


class QRcode(object):
     def __init__(self):
          self.binary="qrencode"
          self.qroutputs="$HOME/Downloads/SRMS-QR"
          if platform == "linux" or platform == "linux2":
               self.binary="qrencode"
          elif platform == "darwin":
               self.binary="qrencode"
          elif platform == "win32":
               self.binary="qrencode.exe"
               self.QRUser=os.environ['USERPROFILE']
               self.path = self.QRUser+"/Downloads/SRMS-QR"
               self.qroutputs=self.path

          #red,blue,green,black,brown
          self.QRforground=["FF0000","4285F4","008000","000000","8B4513","FFFFFF"]
          #black,white
          self.QRbackground=["000000","FFFFFF"]
          

     def BrowseDia(self):
        fname=QFileDialog.getOpenFileName(None,"Choose File","","Text Files (*.txt);;All Files (*)")
        if fname:
          return fname[0]
     
     def setQRcolour(self,x=3):
          
          self.qrRed_White="--foreground="+self.QRforground[0]+" "+"--background="+self.QRbackground[1]
          
          self.qrBlue_White="--foreground="+self.QRforground[1]+" "+"--background="+self.QRbackground[1]
          self.qrGreen_White="--foreground="+self.QRforground[2]+" "+"--background="+self.QRbackground[1]
          self.qrBlack_White="--foreground="+self.QRforground[3]+" "+"--background="+self.QRbackground[1]
          self.qrBrown_White="--foreground="+self.QRforground[4]+" "+"--background="+self.QRbackground[1]
          self.qrWhite_Black="--foreground="+self.QRforground[5]+" "+"--background="+self.QRbackground[0]

          if x==0:
               return self.qrRed_White
          elif x==1:
               return self.qrBlue_White
          elif x==2:
               return self.qrGreen_White
          elif x==3:
               return self.qrBlack_White
          elif x==4:
               return self.qrBrown_White
          elif x==5:
               return self.qrWhite_Black



     def qrgen(self,source="Hello world",filenme="Hello.png",z=4):
          
          if not os.path.exists(self.qroutputs):
               self.makeqroutputs='mkdir  '+self.qroutputs
               os.system(self.makeqroutputs)
          self.colour=self.setQRcolour(z)
          self.toRunQR=self.binary+" "+self.colour+" -s 50 -o"+self.qroutputs+"/"+filenme+".png"+" "+source

          os.system(self.toRunQR)
