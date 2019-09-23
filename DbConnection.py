
from PyQt5 import QtWidgets, QtSql,QtCore
import sys,os


def createConnection():

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    dbPath = QtCore.QCoreApplication.applicationDirPath()
    db.setDatabaseName("voiceAssistant.db")
    db.open()
    if not db.open():
        QtWidgets.QMessageBox.critical(None,"خطا","اتصال به پایگاه داده ممکن نیست", QtWidgets.QMessageBox.Cancel)
        return False
    return True