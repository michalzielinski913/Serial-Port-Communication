from datetime import datetime
from time import sleep
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Dependencies.ConnectionWindow import ConnectionWindow
from Dependencies.CustomNullWindow import CustomNullWindow
from Dependencies.Worker import Worker


class App(QObject):
    '''
    Controller class of the project
    '''
    def __init__(self):

        '''
        Class constructor
        '''
        self.serial=None
        super().__init__()
        import sys
        self.app=QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.terminator = "\r\n"
        self._main_window_set_up(self.MainWindow)
        self.MainWindow.show()
        self.app.exec_()
        self.connection_window = None



    def _main_window_set_up(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_widget = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_widget.setGeometry(QtCore.QRect(50, 80, 500, 250))
        self.input_widget.setObjectName("input_widget")
        self.output_widget = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_widget.setGeometry(QtCore.QRect(50, 460, 500, 250))
        self.output_widget.setReadOnly(True)
        self.output_widget.setObjectName("output_widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 440, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(477, 340, 75, 23))
        self.send_button.setObjectName("send_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(477, 720, 75, 23))
        self.save_button.setObjectName("save_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(380, 720, 75, 23))
        self.clear_button.setObjectName("clear_button")
        self.Ping_button = QtWidgets.QPushButton(self.centralwidget)
        self.Ping_button.setGeometry(QtCore.QRect(60, 370, 93, 28))
        self.Ping_button.setObjectName("Ping_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 380, 55, 16))
        self.label_3.setObjectName("label_3")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(210, 380, 1000, 16))
        self.time_label.setObjectName("time_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuTerminator = QtWidgets.QMenu(self.menubar)
        self.menuTerminator.setObjectName("menuTerminator")
        self.menuStandard = QtWidgets.QMenu(self.menuTerminator)
        self.menuStandard.setObjectName("menuStandard")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNone = QtWidgets.QAction(MainWindow)
        self.actionNone.setCheckable(True)
        self.actionNone.setObjectName("actionNone")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setCheckable(True)
        self.actionCustom.setObjectName("actionCustom")
        self.actionCR = QtWidgets.QAction(MainWindow)
        self.actionCR.setCheckable(True)
        self.actionCR.setObjectName("actionCR")
        self.actionLf = QtWidgets.QAction(MainWindow)
        self.actionLf.setCheckable(True)
        self.actionLf.setObjectName("actionLf")
        self.actionCR_LF = QtWidgets.QAction(MainWindow)
        self.actionCR_LF.setCheckable(True)
        self.actionCR_LF.setChecked(True)
        self.actionCR_LF.setObjectName("actionCR_LF")
        self.menuStandard.addAction(self.actionCR)
        self.menuStandard.addAction(self.actionLf)
        self.menuStandard.addAction(self.actionCR_LF)
        self.menuTerminator.addAction(self.actionNone)
        self.menuTerminator.addAction(self.menuStandard.menuAction())
        self.menuTerminator.addSeparator()
        self.menuTerminator.addAction(self.actionCustom)
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuTerminator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Output:"))
        self.label_2.setText(_translate("MainWindow", "Input:"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.send_button.clicked.connect(self.send_to_serial)
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.menuTerminator.setTitle(_translate("MainWindow", "Terminator"))
        self.menuStandard.setTitle(_translate("MainWindow", "Standard"))

        self.actionNone.setText(_translate("MainWindow", "None"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))
        self.actionCR.setText(_translate("MainWindow", "CR"))
        self.actionLf.setText(_translate("MainWindow", "LF"))
        self.actionCR_LF.setText(_translate("MainWindow", "CR-LF"))

        self.Ping_button.setText(_translate("MainWindow", "PING"))
        self.label_3.setText(_translate("MainWindow", "Time:"))
        self.time_label.setText(_translate("MainWindow", "00:00:00"))

        self.terminator_group=QActionGroup(self)
        self.terminator_group.addAction(self.actionCR)
        self.actionCR.triggered.connect(self.update_terminator)
        self.terminator_group.addAction(self.actionCR_LF)
        self.actionCR_LF.triggered.connect(self.update_terminator)

        self.terminator_group.addAction(self.actionLf)
        self.actionLf.triggered.connect(self.update_terminator)

        self.terminator_group.addAction(self.actionNone)
        self.actionNone.triggered.connect(self.update_terminator)

        self.terminator_group.addAction(self.actionCustom)
        self.actionCustom.triggered.connect(self.update_terminator)

        self.terminator_group.setExclusive(True)

        self.Ping_button.clicked.connect(self.ping_start)


        self.menuConnection.addAction('Set up connection', self._open_connection_window)
    def _open_connection_window(self):
        self.connection_window=QtWidgets.QMainWindow()
        self.connection_ui=ConnectionWindow()
        self.connection_ui.setApp(self)
        self.connection_ui.setupUi(self.connection_window)
        self.connection_window.show()

    def _open_custom_null_window(self):
        self.null_window=QtWidgets.QMainWindow()
        self.null_ui=CustomNullWindow()
        self.null_ui.setApp(self)
        self.null_ui.setupUi(self.null_window)
        self.null_window.show()


    def update_terminator(self):
        if self.actionCR.isChecked():
            self.terminator="\r"
        if self.actionNone.isChecked():
            self.terminator=""
        if self.actionLf.isChecked():
            self.terminator="\n"
        if self.actionCR_LF.isChecked():
            self.terminator="\r\n"
        if self.actionCustom.isChecked():
            self._open_custom_null_window()
        print(self.terminator.encode())
    def connect_test(self):
        print("test")

    def set_output(self, string):
        self.output_widget.setPlainText("test")

    def send_to_serial(self):
        if self.serial is not None:
            payload=self.input_widget.toPlainText()+"{}".format(self.terminator)
            self.serial.write(payload.encode())


    def append_output(self, value):
        self.output_widget.insertPlainText(str(value))

    def setup_connection(self, values):
        port=values[0]
        baud=int(values[1])
        data_field=int(values[2])
        if data_field==7:
            data_field=serial.SEVENBITS
        else:
            data_field=serial.EIGHTBITS

        parity=values[3]
        par=None
        if parity=='Even':
            par=serial.PARITY_EVEN
        elif parity=='Odd':
            par=serial.PARITY_ODD
        else:
            par=serial.PARITY_NONE
        stop=None
        if int(values[4]) == 1:
            stop = serial.STOPBITS_ONE
        else:
            stop = serial.STOPBITS_TWO
        if self.serial is not None:
            if self.serial.is_open:
                self.serial.close()

        self.serial=serial.Serial(port, baudrate=baud, parity=par, stopbits=stop,
                                  bytesize=data_field, dsrdtr=values[5],
                                  rtscts=values[6], xonxoff=values[7], timeout=0.1)
        self.thread=QThread()
        self.worker=Worker()
        self.worker.set_serial(self.serial)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.append_output)
        self.thread.start()


    def ping_start(self):
        if self.serial is not None:
            timestamp=datetime.now()
            self.time_label.setText("Waiting")
            self.time_label.repaint()
            self.serial.write("Test msg".encode())

            while self.serial.in_waiting==0:
                pass

            elapsed=datetime.now()-timestamp
            self.time_label.setText(str(elapsed))
        else:
            self.time_label.setText("No connection detected")
