import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from qepdiff2text.view.view import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())