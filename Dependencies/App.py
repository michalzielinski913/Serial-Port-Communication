
from PyQt5 import QtCore, QtGui, QtWidgets



class App:
    '''
    Controller class of the project
    '''
    def __init__(self):
        '''
        Class constructor
        '''

        import sys
        self.app=QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self._main_window_set_up(self.MainWindow)
        self.MainWindow.show()
        self.app.exec_()
        self.connection_window = ConnectionWindow()

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
        self.menuConnection.addAction('Set up connection', self._open_connection_window)

    def _open_connection_window(self):
        self.connection_window.show()

    def connect_test(self):
        print("test")