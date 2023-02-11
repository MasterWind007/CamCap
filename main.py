import sys  
import cv2
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import uic

import mainWindow 
class ExampleApp(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.playButton.clicked.connect(self.camStart)  
        self.stopButton.clicked.connect(self.camStop)
        self.cap = cv2.VideoCapture(0)
        self.path = r'D:\Documents\PyronProg\CamCap\webcam.png'
        self.image = cv2.imread(self.path)
        #self.path = r'webcam.png'
   
    def camStart(self):
        while True:
            try:
                self.image = self.cap.read()
                cv2.imshow('Camera',self.image)
            except:
                self.image = cv2.imread(self.path)
                ksize = (21, 21)
                self.image = cv2.blur(self.image, ksize)
            self.image = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1]*3, QImage.Format.Format_BGR888)
            self.label.setPixmap(QPixmap(self.image))
            if cv2.waitKey(10) == 27: break
        self.cap.release(self)
        #cv2.destroyAllWindows()

    def camStop(self):
        self.cap.release()

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp()  
    window.show()  
    app.exec()  # 

if __name__ == '__main__':  
    main()  
