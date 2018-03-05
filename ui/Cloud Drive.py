#!/usr/bin/env python3


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloudDrive(object):
    def setupUi(self, CloudDrive):
        CloudDrive.setObjectName("CloudDrive")
        CloudDrive.resize(640, 480)
        CloudDrive.setMinimumSize(QtCore.QSize(640, 480))
        CloudDrive.setMaximumSize(QtCore.QSize(640, 480))
        CloudDrive.setAcceptDrops(False)
        CloudDrive.setStyleSheet("\n"
"background:url(/usr/local/apps/cloud drive/ui\\ components/background);")
        CloudDrive.setTabShape(QtWidgets.QTabWidget.Rounded)
        CloudDrive.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        CloudDrive.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(CloudDrive)
        self.centralwidget.setObjectName("centralwidget")
        self.userImage = QtWidgets.QFrame(self.centralwidget)
        self.userImage.setGeometry(QtCore.QRect(468, 59, 102, 101))
        self.userImage.setStyleSheet("background: url(/usr/local/apps/cloud drive/ui\\ components/userDefaultImage);\n"
"border-radius: 50px;")
        self.userImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userImage.setObjectName("userImage")
        self.logo = QtWidgets.QWidget(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 20, 150, 80))
        self.logo.setStyleSheet("background:url(/usr/local/apps/cloud drive/ui\\ components/logo);")
        self.logo.setObjectName("logo")
        self.optionsWidget = QtWidgets.QWidget(self.centralwidget)
        self.optionsWidget.setGeometry(QtCore.QRect(0, 180, 640, 208))
        self.optionsWidget.setStyleSheet("QWidget#optionsWidget{\n"
"    background:url(/usr/local/apps/cloud drive/ui\\ components/optionsBackground1);\n"
"}\n"
"QWidget#optionsWidget:hover{\n"
"    background:url(/usr/local/apps/cloud drive/ui\\ components/optionsBackground2);\n"
"}\n"
"QWidget#optionsWidget{\n"
"    border-color:transparent\n"
"}")
        self.optionsWidget.setObjectName("optionsWidget")
        self.optionsWidgetChild1 = QtWidgets.QTextBrowser(self.optionsWidget)
        self.optionsWidgetChild1.setGeometry(QtCore.QRect(10, 20, 620, 55))
        self.optionsWidgetChild1.setStyleSheet("QTextBrowser#optionsWidgetChild1{background:#fff;color:#a5a8ab;border:none}\n"
"QTextBrowser#optionsWidgetChild1:hover{background:#eee;}\n"
"")
        self.optionsWidgetChild1.setObjectName("optionsWidgetChild1")
        self.optionsWidgetChild2 = QtWidgets.QTextBrowser(self.optionsWidget)
        self.optionsWidgetChild2.setGeometry(QtCore.QRect(10, 70, 620, 55))
        self.optionsWidgetChild2.setStyleSheet("QTextBrowser#optionsWidgetChild2{background:#fff;border:none;color:#a5a8ab;}\n"
"QTextBrowser#optionsWidgetChild2:hover{background:#eee;}\n"
"")
        self.optionsWidgetChild2.setObjectName("optionsWidgetChild2")
        self.optionsWidgetChild3 = QtWidgets.QTextBrowser(self.optionsWidget)
        self.optionsWidgetChild3.setGeometry(QtCore.QRect(10, 120, 620, 55))
        self.optionsWidgetChild3.setStyleSheet("QTextBrowser#optionsWidgetChild3{background:#fff;border:none;}\n"
"QTextBrowser#optionsWidgetChild3:hover{background:#eee;}\n"
"")
        self.optionsWidgetChild3.setObjectName("optionsWidgetChild3")
        self.checkBox1 = QtWidgets.QCheckBox(self.optionsWidget)
        self.checkBox1.setEnabled(True)
        self.checkBox1.setGeometry(QtCore.QRect(560, 30, 20, 20))
        self.checkBox1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox1.setStyleSheet("background:transparent;\n"
"color:#c5c8cb;\n"
"border:3px solid #c5c8cb;")
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.optionsWidget)
        self.checkBox2.setEnabled(True)
        self.checkBox2.setGeometry(QtCore.QRect(560, 80, 20, 20))
        self.checkBox2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox2.setStyleSheet("background:transparent;\n"
"color:#c5c8cb;\n"
"border:3px solid #c5c8cb;")
        self.checkBox2.setText("")
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.optionsWidget)
        self.checkBox3.setEnabled(True)
        self.checkBox3.setGeometry(QtCore.QRect(560, 130, 20, 20))
        self.checkBox3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox3.setStyleSheet("background:transparent;\n"
"color:#ccc;\n"
"border:3px solid #c5c8cb;")
        self.checkBox3.setText("")
        self.checkBox3.setObjectName("checkBox3")
        self.appDrawerButton = QtWidgets.QFrame(self.centralwidget)
        self.appDrawerButton.setEnabled(True)
        self.appDrawerButton.setGeometry(QtCore.QRect(570, 20, 48, 48))
        self.appDrawerButton.setStyleSheet("QFrame#appDrawerButton{background:url(/usr/local/apps/cloud drive/ui\\ components/appDrawerButton);}QFrame#appDrawerButton:hover{background:url(/usr/local/apps/cloud drive/ui\\ components/appDrawerHoverButton);}")
        self.appDrawerButton.setObjectName("appDrawerButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(490, 420, 130, 48))
        self.quitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quitButton.setStyleSheet("QPushButton#quitButton{border:2px solid #fff ;\n"
"background: url(/usr/local/apps/cloud drive/ui\\ components/exitButton);color:#fff}\n"
"QPushButton#quitButton:hover{border:2px solid #fff ;\n"
"background: url(/usr/local/apps/cloud drive/ui\\ components/exitButtonHover);color:#fff;cursor:pointer}")
        self.quitButton.setText("")
        self.quitButton.setObjectName("quitButton")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(340, 420, 141, 46))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("QPushButton#loginButton{border:2px solid #fff ;\n"
"background: url(/usr/local/apps/cloud drive/ui\\ components/loginButton);color:#fff;text-align:left}\n"
"QPushButton#loginButton:hover{\n"
"background: url(/usr/local/apps/cloud drive/ui\\ components/loginButtonHover);color:#fff;margin-top:2px;}")
        self.loginButton.setObjectName("loginButton")
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(20, 431, 32, 32))
        self.infoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.infoButton.setStyleSheet("QPushButton#infoButton{border:none;\n"
"background: url(/usr/local/apps/cloud drive/ui\\ components/infoButton);}")
        self.infoButton.setText("")
        self.infoButton.setObjectName("infoButton")
        CloudDrive.setCentralWidget(self.centralwidget)

        self.retranslateUi(CloudDrive)
        QtCore.QMetaObject.connectSlotsByName(CloudDrive)

    def retranslateUi(self, CloudDrive):
        _translate = QtCore.QCoreApplication.translate
        CloudDrive.setWindowTitle(_translate("CloudDrive", "Cloud Drive"))
        self.optionsWidgetChild1.setHtml(_translate("CloudDrive", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#555753;\">    Start the Application at startup</span></p></body></html>"))
        self.optionsWidgetChild2.setHtml(_translate("CloudDrive", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#555753;\">    Show Notifications</span></p></body></html>"))
        self.optionsWidgetChild3.setHtml(_translate("CloudDrive", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#555753;\">    Add bookmark to Nautilus</span></p></body></html>"))
        self.checkBox1.setText(_translate("CloudDrive", "d"))
        self.loginButton.setText(_translate("CloudDrive", "       LOGOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CloudDrive = QtWidgets.QMainWindow()
    ui = Ui_CloudDrive()
    ui.setupUi(CloudDrive)
    CloudDrive.show()
    sys.exit(app.exec_())

