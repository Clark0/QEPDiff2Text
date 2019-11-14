# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseConnection.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from qepdiff2text.QEPFetcher import QEPFetcher
import psycopg2


class ConnectHelper(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(591, 221)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.dbName = QtWidgets.QLabel(Dialog)
        self.dbName.setObjectName("dbName")
        self.gridLayout.addWidget(self.dbName, 1, 0, 1, 2)
        self.dbName_line = QtWidgets.QLineEdit(Dialog)
        self.dbName_line.setObjectName("dbName_line")
        self.gridLayout.addWidget(self.dbName_line, 1, 2, 1, 1)
        self.hostName = QtWidgets.QLabel(Dialog)
        self.hostName.setObjectName("hostName")
        self.gridLayout.addWidget(self.hostName, 2, 0, 1, 1)
        self.username = QtWidgets.QLabel(Dialog)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 3, 0, 1, 1)
        self.password = QtWidgets.QLabel(Dialog)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 4, 0, 1, 1)
        self.port = QtWidgets.QLabel(Dialog)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 5, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(self.get_input)

        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)

        self.hostName_line = QtWidgets.QLineEdit(Dialog)
        self.hostName_line.setObjectName("hostName_line")
        self.gridLayout.addWidget(self.hostName_line, 2, 2, 1, 1)

        self.username_line = QtWidgets.QLineEdit(Dialog)
        self.username_line.setObjectName("username_line")
        self.gridLayout.addWidget(self.username_line, 3, 2, 1, 1)

        self.password_line = QtWidgets.QLineEdit(Dialog)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.gridLayout.addWidget(self.password_line, 4, 2, 1, 1)

        self.port_line = QtWidgets.QLineEdit(Dialog)
        self.port_line.setObjectName("port_line")
        self.gridLayout.addWidget(self.port_line, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.qep_fetcher = None

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Database connection"))
        self.dbName.setText(_translate("Dialog", "Database Name"))
        self.hostName.setText(_translate("Dialog", "Host Name"))
        self.username.setText(_translate("Dialog", "Username"))
        self.password.setText(_translate("Dialog", "Password"))
        self.port.setText(_translate("Dialog", "Port"))

        self.dbName_line.setText('TPC-H')
        self.hostName_line.setText('localhost')
        self.username_line.setText('postgres')
        self.password_line.setText('mysecretpassword')
        self.port_line.setText('')

    def get_input(self):
        db_info = []
        database = self.dbName_line.text()
        host = self.hostName_line.text()
        user = self.username_line.text()
        password = self.password_line.text()
        port = self.port_line.text()

        try:
            self.qep_fetcher = QEPFetcher(host=host, dbname=database, user=user, password=password, port= port)
        except psycopg2.Error as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
