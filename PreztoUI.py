# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtWidgets
import Logo_rc
import os
import operator
from Function import *
from selenium import webdriver
from PIL import Image
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import *
from selenium.webdriver.chrome.options import Options
from PyPDF2 import PdfFileMerger


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Prezto")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.pushButton.setObjectName("Get Prezi")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 160, 271, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 30, 241, 121))
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Button that starts the conversion process</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.textEdit.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Text box for address of prezi</p><p><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Prezto logo</p><p><br/></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/image/prezto.png\"/></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
