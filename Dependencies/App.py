import tkinter as tk

from Dependencies.Views.GUI import GUI
from PyQt5 import QtWidgets

class App:
    '''
    Controller class of the project
    '''
    def __init__(self):
        '''
        Class constructor
        '''
        self.gui=GUI()
        import sys
        self.app=QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.gui.setupUi(self.MainWindow)
        self.MainWindow.show()
