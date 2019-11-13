# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import logging
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QCheckBox, QListWidgetItem, QTableWidgetItem, QDialog, QPushButton, QMessageBox, QToolTip
from qepdiff2text.view.connection import ConnectHelper
from qepdiff2text.get_des import get_des
from qepdiff2text.Node import Node
from qepdiff2text.Description import DeletionDescription, InsertionDescription, UpdateDescription, SameDescription


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.query_list = []
        self.query_nb = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Connction = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Connction.sizePolicy().hasHeightForWidth())
        self.Connction.setSizePolicy(sizePolicy)
        self.Connction.setMinimumSize(QtCore.QSize(0, 35))
        self.Connction.setObjectName("Connction")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Connction)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.Connction)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet('color: red')
        self.horizontalLayout_4.addWidget(self.label_6)
        self.connectBtn = QtWidgets.QPushButton(self.Connction)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_4.addWidget(self.connectBtn)
        self.verticalLayout_6.addWidget(self.Connction)
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.frame = QtWidgets.QFrame(self.splitter_2)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.historyLabel = QtWidgets.QLabel(self.widget)
        self.historyLabel.setMaximumSize(QtCore.QSize(16777215, 211))
        self.historyLabel.setObjectName("historyLabel")
        self.horizontalLayout.addWidget(self.historyLabel)
        self.clearBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        self.clearBtn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        self.clearBtn.setFont(font)
        self.clearBtn.setAutoRepeatDelay(301)
        self.clearBtn.setAutoRepeatInterval(105)
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout.addWidget(self.clearBtn)
        self.verticalLayout_3.addWidget(self.widget)
        self.queryhistoryWidget = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryhistoryWidget.sizePolicy().hasHeightForWidth())
        self.queryhistoryWidget.setSizePolicy(sizePolicy)
        self.queryhistoryWidget.setObjectName("queryhistoryWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.queryhistoryWidget)
        self.gridLayout.setContentsMargins(-1, 0, -1, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.queryhistoryWidget)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.loadBtn = QtWidgets.QPushButton(self.queryhistoryWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadBtn.sizePolicy().hasHeightForWidth())
        self.loadBtn.setSizePolicy(sizePolicy)
        self.loadBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout.addWidget(self.loadBtn, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.queryhistoryWidget)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.InputSection = QtWidgets.QFrame(self.splitter)
        self.InputSection.setObjectName("InputSection")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InputSection)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputLabel = QtWidgets.QLabel(self.InputSection)
        self.inputLabel.setObjectName("inputLabel")
        self.horizontalLayout_2.addWidget(self.inputLabel, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.inputBox = QtWidgets.QTextEdit(self.InputSection)
        self.inputBox.setObjectName("inputBox")

        self.addBtn = QtWidgets.QPushButton(self.InputSection)
        self.addBtn.setObjectName("addBtn")
        self.addBtn.clicked.connect(self.get_input)

        self.horizontalLayout_2.addWidget(self.addBtn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.addWidget(self.inputBox)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.query1_label = QtWidgets.QLabel(self.layoutWidget)
        self.query1_label.setObjectName("query1_label")
        self.verticalLayout_4.addWidget(self.query1_label)
        self.query1_box = QtWidgets.QTextEdit(self.layoutWidget)
        self.query1_box.setReadOnly(True)
        self.query1_box.setMinimumSize(QtCore.QSize(100, 50))
        self.query1_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.query1_box.setToolTipDuration(0)
        self.query1_box.setObjectName("query1_box")
        self.verticalLayout_4.addWidget(self.query1_box)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.query2_label = QtWidgets.QLabel(self.layoutWidget)
        self.query2_label.setObjectName("query2_label")
        self.verticalLayout_5.addWidget(self.query2_label)
        self.query2_box = QtWidgets.QTextEdit(self.layoutWidget)
        self.query2_box.setReadOnly(True)
        self.query2_box.setObjectName("query2_box")
        self.verticalLayout_5.addWidget(self.query2_box)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.widget1 = QtWidgets.QWidget(self.splitter_3)

        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        header = self.tableWidget.horizontalHeader()
        #
        header.setSectionResizeMode(0, 1)
        header.setSectionResizeMode(1, 1)
        header.setSectionResizeMode(2, 1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.splitter_3)

        self.verticalLayout_6.addWidget(self.splitter_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "❌Not connected"))
        self.connectBtn.setText(_translate("MainWindow", "Connect"))
        self.connectBtn.clicked.connect(self.onConnectionClick)
        self.historyLabel.setText(_translate("MainWindow", "History"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.clearBtn.clicked.connect(self.clear_list)

        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.loadBtn.clicked.connect(self.getChoose)

        self.inputLabel.setText(_translate("MainWindow", "InputBox"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.query1_label.setText(_translate("MainWindow", "Query1"))
        self.query2_label.setText(_translate("MainWindow", "Query2"))
        self.label.setText(_translate("MainWindow", "Difference"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "query1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "query2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "difference"))
        self.qep_fetcher = None

    def insert(self, data_list):
        """
        """
        # for i in data_list:
        i = data_list[-1]
        self.query_nb += 1
        box = QCheckBox('query_' + str(self.query_nb))
        item = QListWidgetItem()

        self.listWidget.addItem(item)
        # self.listWidget.addItem(query_doc)
        self.listWidget.setItemWidget(item, box)
        self.listWidget.addItem(i)

    def get_input(self, input_list):
        doc = self.inputBox.document().toPlainText()
        self.query_list.append(doc)
        self.insert(self.query_list)

    def clear_list(self):
        self.listWidget.clear()
        self.query_list = []

    def getChoose(self) -> [str]:


        count = self.listWidget.count()  # QListWidget的总个数

        cb_list = [self.listWidget.itemWidget(self.listWidget.item(i))
                   for i in range(0, count, 2)]  # QListWidget里面所有QListWidgetItem中的QCheckBox
        chooses = []
        for cb in cb_list:  # type:QCheckBox
            if cb.isChecked():
                j = 2*(int(str(cb.text())[-1]))-1
                chooses.append(self.listWidget.item(j).text())
        if len(chooses) != 2:
            msg = QMessageBox()
            msg.setText("Please check exactly two queries for comparison")
            msg.exec_()
            return

        # print(chooses)
        self.query1_box.setText(chooses[0])
        self.query2_box.setText(chooses[1])

        if self.qep_fetcher:
            analyze_bef = self.qep_fetcher.fetch_json(chooses[0])
            analyze_aft = self.qep_fetcher.fetch_json(chooses[1])
            if analyze_bef and analyze_aft:
                self.set_table(self.get_diff(analyze_bef, analyze_aft))
            else:
                logger = logging.getLogger("view.qepdiff")
                logger.error('fail to query qep')
        else:
            msg = QMessageBox()
            msg.setText("Database is not connected.")
            msg.exec_()
            return
        return chooses

    def get_diff(self, analyze_bef, analyze_aft):
        node_bef, node_aft = Node(analyze_bef), Node(analyze_aft)
        return get_des(node_bef, node_aft)

    def set_table(self, lst):
        rows = len(lst)
        self.tableWidget.setRowCount(rows)
        for i in range(rows):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(lst[i].get_before_des()))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(lst[i].get_after_des()))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(lst[i].get_diff_des()))
            if isinstance(lst[i], UpdateDescription):
                self.tableWidget.item(i, 0).setBackground(QtGui.QColor(255, 242, 204, 127))
                self.tableWidget.item(i, 1).setBackground(QtGui.QColor(255, 242, 204, 127))
                self.tableWidget.item(i, 2).setBackground(QtGui.QColor(255, 242, 204, 127))

            if isinstance(lst[i], DeletionDescription):
                self.tableWidget.item(i, 0).setBackground(QtGui.QColor(244, 204, 204, 127))
                self.tableWidget.item(i, 1).setBackground(QtGui.QColor(244, 204, 204, 127))
                self.tableWidget.item(i, 2).setBackground(QtGui.QColor(244, 204, 204, 127))


            if isinstance(lst[i], InsertionDescription):
                self.tableWidget.item(i, 0).setBackground(QtGui.QColor(217, 234, 211, 127))
                self.tableWidget.item(i, 1).setBackground(QtGui.QColor(217, 234, 211, 127))
                self.tableWidget.item(i, 2).setBackground(QtGui.QColor(217, 234, 211, 127))


    def onConnectionClick(self, s):
        logger = logging.getLogger('view.connect')
        dialog = QDialog()
        dialogHelper = ConnectHelper()
        dialogHelper.setupUi(dialog)
        dialog.exec_()
        self.qep_fetcher = dialogHelper.qep_fetcher
        QToolTip.setFont(QtGui.QFont('SansSerif', 20))

        if self.qep_fetcher is not None:
            logger.info('db connected')
            QToolTip.showText(QtCore.QPoint(500, 200), "Connected Successfully!")
            self.label_6.setStyleSheet('color: green')
            self.label_6.setText("Connected Successfully")
        else:
            logger.info('connection fail')
            QToolTip.showText(QtCore.QPoint(500, 200), "Connection Failed, please try again.")
            self.label_6.setStyleSheet('color: red')
            self.label_6.setText("Connection Failed")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
