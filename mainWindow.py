# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 138)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.playButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.playButton.setObjectName("playButton")
        self.verticalLayout_7.addWidget(self.playButton)
        self.T1Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.T1Button.setObjectName("T1Button")
        self.verticalLayout_7.addWidget(self.T1Button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_6.addWidget(self.stopButton)
        self.T2Button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.T2Button_2.setObjectName("T2Button_2")
        self.verticalLayout_6.addWidget(self.T2Button_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.findCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.findCheckBox.setObjectName("findCheckBox")
        self.verticalLayout_3.addWidget(self.findCheckBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(1, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.effectListcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.effectListcomboBox.setMaxVisibleItems(5)
        self.effectListcomboBox.setObjectName("effectListcomboBox")
        self.effectListcomboBox.addItem("")
        self.effectListcomboBox.addItem("")
        self.effectListcomboBox.addItem("")
        self.effectListcomboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.effectListcomboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_5.addWidget(self.horizontalSlider)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.connCamButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.connCamButton.setObjectName("connCamButton")
        self.verticalLayout_4.addWidget(self.connCamButton)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionClose = QtGui.QAction(parent=MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Start"))
        self.T1Button.setText(_translate("MainWindow", "T1Button"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.T2Button_2.setText(_translate("MainWindow", "T2Button"))
        self.findCheckBox.setText(_translate("MainWindow", "Find plata"))
        self.label_2.setText(_translate("MainWindow", "Effects"))
        self.effectListcomboBox.setItemText(0, _translate("MainWindow", "None"))
        self.effectListcomboBox.setItemText(1, _translate("MainWindow", "Blur"))
        self.effectListcomboBox.setItemText(2, _translate("MainWindow", "Canny"))
        self.effectListcomboBox.setItemText(3, _translate("MainWindow", "Grey"))
        self.connCamButton.setText(_translate("MainWindow", "Connect Cam"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))



def resWindow():
    MainWindow.resize(10, 10)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
