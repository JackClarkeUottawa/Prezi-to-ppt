# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreztoUI2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Function import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.Start.setObjectName("Start")
        self.Start.clicked.connect(self.starttheshow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 241, 121))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 150, 281, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.returnPressed.connect(self.starttheshow)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 251, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setAccessibleName(_translate("MainWindow", "Prezto Window"))
        self.Start.setAccessibleName(_translate("MainWindow", "Button to start program"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.label.setAccessibleName(_translate("MainWindow", "Prezto Logo"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/image/prezto.png\"/></p></body></html>"))
        self.plainTextEdit.setAccessibleName(_translate("MainWindow", "Input Box for Prezi URL"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", " https://prezi.com/view/ABCDEFGHIJKLMNOP/"))
        self.label_2.setText(_translate("MainWindow", "Enter Your URL and press enter or click START!"))

    def starttheshow(self):
        #self.label_2.setText("Processing Your Prezi! This may take several minutes.")
        main(self.plainTextEdit.text())
        #self.label_2.setText("Done!")
import Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
