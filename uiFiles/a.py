# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloudDrive(object):
    def setupUi(self, CloudDrive):
        CloudDrive.setObjectName("CloudDrive")
        CloudDrive.setEnabled(False)
        CloudDrive.resize(640, 480)
        CloudDrive.setMinimumSize(QtCore.QSize(640, 480))
        CloudDrive.setMaximumSize(QtCore.QSize(640, 480))
        CloudDrive.setAcceptDrops(False)
        CloudDrive.setStyleSheet("background-color: #ccc")
        CloudDrive.setIconSize(QtCore.QSize(48, 48))
        CloudDrive.setTabShape(QtWidgets.QTabWidget.Rounded)
        CloudDrive.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        CloudDrive.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(CloudDrive)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, -130, 512, 371))
        self.widget.setStyleSheet("background:url(/run/media/prateek/EC3096E23096B356/Users/Prateek Agrawal/Google Drive/projects/mini-project/cloud drive/components/logo/512x512.png)")
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 250, 621, 221))
        font = QtGui.QFont()
        font.setFamily("Futura Lt BT")
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border:none;")
        self.textBrowser.setObjectName("textBrowser")
        CloudDrive.setCentralWidget(self.centralwidget)

        self.retranslateUi(CloudDrive)
        QtCore.QMetaObject.connectSlotsByName(CloudDrive)

    def retranslateUi(self, CloudDrive):
        _translate = QtCore.QCoreApplication.translate
        CloudDrive.setWindowTitle(_translate("CloudDrive", "Cloud Drive"))
        self.textBrowser.setHtml(_translate("CloudDrive", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Futura Lt BT\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-weight:400;\">                                                             </span><span style=\" font-family:\'Cantarell\'; font-size:14pt; color:#cc6356;\">Cloud Drive</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; color:#555753;\">                                                              </span><span style=\" font-family:\'Cantarell\'; font-size:9pt; color:#555753;\">    </span><span style=\" font-family:\'Cantarell\'; font-size:9pt; font-style:italic; color:#555753;\">version : 1.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:9pt; font-style:italic; color:#555753;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-style:italic; color:#555753;\">                                            </span><span style=\" font-family:\'Cantarell\'; font-style:italic; color:#c4a000;\">An unofficial client for Google Drive</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-style:italic; color:#555753;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:10pt; color:#cc6356;\">Synchronizes your Google Drive data with your Desktop. Gives notification for synchronization of every file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:10pt; color:#555753;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:10pt; color:#555753;\">                              Developed by Prateek Agrawal </span><a href=\"mailto://prateekagrawal89760@gmail.com\"><span style=\" font-family:\'Cantarell\'; font-weight:400; text-decoration: underline; color:#0000ff;\">prateekagrawal89760@gmail.com</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:10pt; color:#555753;\">                                        </span><a href=\"https://www.github.com/prateek89760/cloud-drive\"><span style=\" font-family:\'Cantarell\'; font-weight:400; text-decoration: underline; color:#0000ff;\">https://www.github.com/prateek89760/cloud-drive</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CloudDrive = QtWidgets.QMainWindow()
    ui = Ui_CloudDrive()
    ui.setupUi(CloudDrive)
    CloudDrive.show()
    sys.exit(app.exec_())

