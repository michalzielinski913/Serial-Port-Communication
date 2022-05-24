from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox


class CustomNullWindow(object):
    def setupUi(self, Form):
        self.window = Form
        Form.setObjectName("Form")
        Form.resize(452, 165)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(100, 100, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self._close_window)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def setApp(self, app):
        self.app=app

    def _close_window(self):
        self.app.terminator=self.lineEdit.text()
        self.app.terminator=r"{}".format(self.app.terminator)
        print(repr(self.app.terminator.replace(r"\\", "\\")))
        self.window.close()
