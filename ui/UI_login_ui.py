# Form implementation generated from reading ui file 'd:\ML\Final\MLBA-Factory-Management\ui\UI_login.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"#widget{\n"
"    background-color:rgb(9,27,68);\n"
"    border-radius: 20px;\n"
"}\n"
"QLineEdit{\n"
"     background-color:rgb(9,10,37);\n"
"    padding: 5px 3px;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:rgb(9,10,37);\n"
"    padding: 10px 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#to_login_2, #to_register_2{\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 20, 300, 500))
        self.widget.setMinimumSize(QtCore.QSize(300, 500))
        self.widget.setMaximumSize(QtCore.QSize(300, 500))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.registerPage_2 = QtWidgets.QWidget()
        self.registerPage_2.setObjectName("registerPage_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.registerPage_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(parent=self.registerPage_2)
        self.label_9.setMinimumSize(QtCore.QSize(70, 70))
        self.label_9.setMaximumSize(QtCore.QSize(70, 70))
        self.label_9.setStyleSheet("")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("d:\\ML\\Final\\MLBA-Factory-Management\\ui\\../image/img_add-user.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(parent=self.registerPage_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_11 = QtWidgets.QLabel(parent=self.registerPage_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(parent=self.registerPage_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_8.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_8.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.frame_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_8.addWidget(self.checkBox_2)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.registerPage_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.to_login_2 = QtWidgets.QPushButton(parent=self.registerPage_2)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.to_login_2.setFont(font)
        self.to_login_2.setObjectName("to_login_2")
        self.verticalLayout_7.addWidget(self.to_login_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(parent=self.registerPage_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.stackedWidget.addWidget(self.registerPage_2)
        self.loginPage_2 = QtWidgets.QWidget()
        self.loginPage_2.setObjectName("loginPage_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.loginPage_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(parent=self.loginPage_2)
        self.label_13.setMinimumSize(QtCore.QSize(70, 70))
        self.label_13.setMaximumSize(QtCore.QSize(70, 70))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("d:\\ML\\Final\\MLBA-Factory-Management\\ui\\../image/img_add-user.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(parent=self.loginPage_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_4 = QtWidgets.QFrame(parent=self.loginPage_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_10.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_10.addWidget(self.lineEdit_10, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_9.addWidget(self.frame_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.label_15 = QtWidgets.QLabel(parent=self.loginPage_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.loginPage_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_9.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.to_register_2 = QtWidgets.QPushButton(parent=self.loginPage_2)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.to_register_2.setFont(font)
        self.to_register_2.setObjectName("to_register_2")
        self.verticalLayout_9.addWidget(self.to_register_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(parent=self.loginPage_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.stackedWidget.addWidget(self.loginPage_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("d:\\ML\\Final\\MLBA-Factory-Management\\ui\\../image/img_Creative-Uses-of-HR-Technology.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_17.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Sign Up"))
        self.label_11.setText(_translate("MainWindow", "Enter your information below"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Confirm Pasword"))
        self.checkBox_2.setText(_translate("MainWindow", "Agree with our terms"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.to_login_2.setText(_translate("MainWindow", "Already registered? Login"))
        self.label_12.setText(_translate("MainWindow", "WabiSabi Group."))
        self.label_14.setText(_translate("MainWindow", "Log In"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_15.setText(_translate("MainWindow", "Enter your information below"))
        self.pushButton_4.setText(_translate("MainWindow", "Login"))
        self.to_register_2.setText(_translate("MainWindow", "Not registered? Register"))
        self.label_16.setText(_translate("MainWindow", "WabiSabi Group."))