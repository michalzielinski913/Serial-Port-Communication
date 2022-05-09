import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

from Dependencies.ConnectionWindow import ConnectionWindow
from Dependencies.Worker import Worker


class App:
    '''
    Controller class of the project
    '''
    def __init__(self):
        '''
        Class constructor
        '''
        self.serial=None
        import sys
        self.app=QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConnection.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSI Project"))
        self.label.setText(_translate("MainWindow", "Output:"))
        self.label_2.setText(_translate("MainWindow", "Input:"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.send_button.clicked.connect(self.send_to_serial)

        self.menuConnection.addAction('Set up connection', self._open_connection_window)
    def _open_connection_window(self):
        self.connection_window=QtWidgets.QMainWindow()
        self.connection_ui=ConnectionWindow()
        self.connection_ui.setApp(self)
        self.connection_ui.setupUi(self.connection_window)
        self.connection_window.show()

    def connect_test(self):
        print("test")

    def set_output(self, string):
        self.output_widget.setPlainText("test")

    def send_to_serial(self):
        if self.serial is not None:
            self.serial.write(self.input_widget.toPlainText().encode())

    def append_output(self, value):
        self.output_widget.appendPlainText(str(value))

    def setup_connection(self, values):
        port=values[0]
        baud=int(values[1])
        data_field=int(values[2])
        parity=values[3]
        if parity=='Even':
            par=serial.PARITY_EVEN
        elif parity=='Odd':
            par=serial.PARITY_ODD
        else:
            par=serial.PARITY_NONE
        stop=int(values[4])
        self.serial=serial.Serial(port, baudrate=baud)
        self.thread=QThread()
        self.worker=Worker()
        self.worker.set_serial_and_window(self.serial, self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.append_output)
        self.thread.start()

