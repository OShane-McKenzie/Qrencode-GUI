from PyQt5 import QtCore, QtWidgets
from QRcode import QRcode
import os
import sys
from sys import platform
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.p=0
        self.QRcolourList=["Red-White","Blue-White","Green-White","Black-White","Brown-White","White-Black"]
        self.QRcodeObjects=QRcode()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 745)
        MainWindow.setFixedSize(1177, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 1151, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 120, 891, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 250, 251, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 290, 1151, 61))
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItems(self.QRcolourList)
        

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 10, 300, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 90, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 470, 1131, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.getFname)
        self.pushButton_2.clicked.connect(self.generateQR)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR Generator. By: O'Shane McKenzie"))
        self.pushButton.setText(_translate("MainWindow", "Browse for text file"))
        self.label.setText(_translate("MainWindow", "Foreground-Background"))
        self.label_2.setText(_translate("MainWindow", "Type text to generate QR code"))
        self.label_3.setText(_translate("MainWindow", "OR"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate QR Code"))

    def getFname(self):
        self.fnamePath=self.QRcodeObjects.BrowseDia()
        self.lineEdit.setText(self.fnamePath)
        
    def generateQR(self):
        self.colourText=self.comboBox.currentText()
        self.getIndex=self.comboBox.findText(self.colourText, QtCore.Qt.MatchFixedString)
        self.qrSource=self.lineEdit.text()
        self.lineCounter=0
        
        isFileFound=os.path.exists(self.qrSource)
        if isFileFound==True:
            self.QRsourceFile=os.path.basename(self.qrSource)
            with open(self.qrSource,'r') as Qlines:
                lines = Qlines.readlines()
            for line in lines:
                self.shellLine=f'"{line}"'
                self.QRcodeObjects.qrgen(self.shellLine,self.QRsourceFile.replace('.txt','_')+str(self.lineCounter),self.getIndex)
                self.lineCounter+=1
            self.QRUser=os.environ['USERPROFILE']
            self.path = self.QRUser+"/Downloads/SRMS-QR"
            self.lineEdit.setText("QR has been generated!")
            if platform == "linux" or platform == "linux2":
                 subprocess.call(["xdg-open", "$HOME/Downloads"])
            elif platform == "darwin":
                subprocess.call(["open", "$HOME/Downloads"])
            elif platform == "win32":
                os.startfile(self.path)
        else:
            line=self.qrSource
            self.shellLine=f'"{line}"'
            self.QRcodeObjects.qrgen(self.shellLine,self.shellLine.replace(' ','_'),self.getIndex)

            if platform == "linux" or platform == "linux2":

                 os.system('xdg-open "%s"' % "$HOME/Downloads")
            elif platform == "darwin":
                os.system('open "%s"' % "$HOME/Downloads")

            elif platform == "win32":
                self.QRUser=os.environ['USERPROFILE']
                self.path = self.QRUser+"/Downloads/SRMS-QR"
                os.startfile(self.path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
