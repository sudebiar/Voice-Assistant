
from PyQt5 import QtWidgets, QtSql,QtCore

def createConnection():

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    dbPath = QtCore.QCoreApplication.applicationDirPath()
    db.setDatabaseName("voiceAssistant.db")
    db.open()
    if not db.open():
        QtWidgets.QMessageBox.critical(None,"خطا","امکان وصل شدن به پایگاه داده وجود ندارد", QtWidgets.QMessageBox.Cancel)
        return False
    return True