import sys  
import cv2
import keyboard
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import mainWindow
import neiro as nf 

class ExampleApp(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.playButton.clicked.connect(self.camStart)  
        self.stopButton.clicked.connect(self.camStop)
        self.effectListcomboBox.activated.connect(self.onComboActivated)
        self.horizontalSlider.sliderMoved.connect(self.onSliderMoved)
        self.findCheckBox.stateChanged.connect(self.onFcbChek)
        self.path = r'webcam.png'
        self.ret = False
        self.curEff = 0
        self.slPos = 0
        self.findF = False
        self.ni = nf.neiroFind('nero\platanumber.xml')

    def mat2rgb(self,frame):
            fr = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QImage.Format.Format_BGR888)
            return QPixmap(fr)

    def camStart(self):
        #self.cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture('car1.mp4') 
        while True:
            ret, frame = cap.read()
            if not ret:
                frame = cv2.imread(self.path)
            if self.findF:
                frame = self.ni.findFace(self.switchEffects(frame, self.curEff))
            else:
                frame = self.switchEffects(frame, self.curEff)    
            self.label.setPixmap(self.mat2rgb(frame))
            cv2.waitKey(0)
            if keyboard.is_pressed(chr(27)): 
                break
             
        ret = False
        frame = cv2.imread(self.path)
        self.label.setPixmap(self.mat2rgb(frame))
        self.label.update()
        cap.release()
        self.resize(494, 138)
        
        

             


    def switchEffects(self, img ,ef):
        if ef == 0: return img
        if ef == 1: return cv2.GaussianBlur(img, (19, 19),0)
        if ef == 2:
            im =  cv2.Canny(img, self.slPos*6, self.slPos*6)
            return cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
        if ef == 3: 
            im =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)

    
    def onComboActivated(self):
        self.curEff = self.effectListcomboBox.currentIndex()

    def onSliderMoved(self, mov):
        self.slPos = self.horizontalSlider.sliderPosition()

    def camStop(self):
       self.resize(494, 138)
       
       
       

    def onFcbChek(self):
        self.findF = self.findCheckBox.isChecked()




def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp()  
    window.show()  
    app.exec()  # 

if __name__ == '__main__':  
    main()
