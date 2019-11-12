from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sys
#创建数据库连接
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView


def createConnection():
    #选择数据库类型，这里为mysql数据库
    db=QSqlDatabase.addDatabase("QPSQL")
    db.setDatabaseName("you_db")
    db.setHostName("localhost")  #set address
    db.setUserName("you_usr"); #set user name
    db.setPassword("you_passwd"); #set user pwd
    #打开数据库
       #打开数据库
    if (db.open()):
      print ("Success")
    else:
      print ("Failed to connect to mysql")
#创建表
def createTable():
    #创建QsqlQuery对象，用于执行sql语句
    q=QSqlQuery()
    q.exec_("create table if not exists t1 (f1 integer primary key,f2 varchar(20))")
    q.exec_("delete from t1")
    #这里使用 u 将字符串转换成unicode编码，解决中文乱码
    q.exec_(u"insert into t1 values(1,'我')")
    q.exec_(u"insert into t1 values(2,'我')")
    q.exec_("commit")

class Model(QSqlTableModel):
    def __init__(self,parent):
        QSqlTableModel.__init__(self,parent)
        #设置要载入的表名
        self.setTable("t1")
        #这一步应该是执行查询的操作
        self.select()
        #数据更新的策略，详细可以查看Qt文档
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)

class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        vbox=QVBoxLayout(self)
        self.view=QTableView()
        self.model=Model(self.view)
        self.view.setModel(self.model)
        vbox.addWidget(self.view)

if __name__=="__main__":
    a=QApplication(sys.argv)
    createConnection()
    createTable()
    w=TestWidget()
    w.show()
    sys.exit(a.exec_())