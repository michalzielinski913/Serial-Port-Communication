from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time

from serial import PortNotOpenError


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def set_serial(self, serial):
        self.serial=serial

    def run(self):
        """Long-running task."""
        while True:
                result=self.serial.read()
                self.progress.emit(result.decode())


        self.finished.emit()