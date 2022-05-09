import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDialogButtonBox

from Dependencies.serial_functions import get_com_ports


class ConnectionWindow(object):
    def __init__(self):
        '''
        Class constructor
        '''
        self.baud_rates=["150","300", "600", "1200", "2400", "4800", "9600", "115200"]
        self.data_fields=["7", "8"]
        self.parity_control=["Even", "Odd", "None"]
        self.stop_bits=["1", "2"]
    def setupUi(self, COMSetup):
        self.window=COMSetup
        COMSetup.setObjectName("COMSetup")
        COMSetup.resize(300, 399)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(COMSetup.sizePolicy().hasHeightForWidth())
        COMSetup.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(COMSetup)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(30, 220, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_window)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(COMSetup.close)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self._refresh_com_ports()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 44, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 40, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self._refresh_com_ports)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 74, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 70, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(self.baud_rates)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 124, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 120, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(self.data_fields)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 154, 47, 13))
        self.label_5.setObjectName("label_5")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(70, 150, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItems(self.parity_control)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 184, 47, 13))
        self.label_6.setObjectName("label_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 180, 69, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItems(self.stop_bits)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        COMSetup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(COMSetup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 252, 26))
        self.menubar.setObjectName("menubar")
        COMSetup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(COMSetup)
        self.statusbar.setObjectName("statusbar")
        COMSetup.setStatusBar(self.statusbar)

        self.retranslateUi(COMSetup)
        QtCore.QMetaObject.connectSlotsByName(COMSetup)

    def retranslateUi(self, COMSetup):
        _translate = QtCore.QCoreApplication.translate
        COMSetup.setWindowTitle(_translate("COMSetup", "COM port setup"))
        self.label.setText(_translate("COMSetup", "COM Port:"))
        self.pushButton.setText(_translate("COMSetup", "Refresh"))
        self.label_2.setText(_translate("COMSetup", "Bit Rate"))
        self.label_3.setText(_translate("COMSetup", "Data Field"))
        self.label_4.setText(_translate("COMSetup", "Protocol Data Unit:"))
        self.label_5.setText(_translate("COMSetup", "Parity"))
        self.label_6.setText(_translate("COMSetup", "Stop Bits"))
        self.label_7.setText(_translate("COMSetup", "COM Port setup"))

    def _refresh_com_ports(self):
        self.comboBox.clear()
        self.comboBox.addItems(get_com_ports())

    def get_com_port(self):
        return self.comboBox.currentText()

    def setApp(self, app):
        self.app=app
        #self.app.connect_test()

    def close_window(self):
        items=[self.comboBox.currentText(), self.comboBox_2.currentText(), self.comboBox_3.currentText(), self.comboBox_4.currentText(), self.comboBox_5.currentText()]
        self.app.setup_connection((items))

        self.window.close()


