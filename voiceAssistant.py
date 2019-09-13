# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets ,QtSql
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,os , webbrowser
import SpeechCls
from PyQt5.QtCore import pyqtSignal, QObject
import DbConnection
from googletrans import Translator
import webbrowser
from FormAdd import Ui_frmAdd



class Communicate(QObject):
    
    processSignal = pyqtSignal()  

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboMic = QtWidgets.QComboBox(self.centralwidget)
        self.comboMic.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboMic.setObjectName("comboMic")
        self.verticalLayout_2.addWidget(self.comboMic)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.comboLng = QtWidgets.QComboBox(self.centralwidget)
        self.comboLng.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboLng.setObjectName("comboLng")
        self.comboLng.addItem("")
        self.comboLng.addItem("")
        self.comboLng.addItem("")
        self.comboLng.addItem("")
        self.comboLng.addItem("")
        self.verticalLayout_4.addWidget(self.comboLng)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.btnSpeak = QtWidgets.QPushButton(self.centralwidget)
        self.btnSpeak.setMaximumSize(QtCore.QSize(16777215, 600))
        self.btnSpeak.setObjectName("btnSpeak")
        self.btnSpeak.setIcon(QIcon("mic.png"))
        self.btnSpeak.setIconSize(QtCore.QSize(65, 65));
        self.verticalLayout_3.addWidget(self.btnSpeak)
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnRefresh.setObjectName("btnRefresh")
        self.verticalLayout_3.addWidget(self.btnRefresh)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.textVoice = QtWidgets.QTextEdit(self.centralwidget)
        self.textVoice.setObjectName("textVoice")
        self.verticalLayout.addWidget(self.textVoice)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnClr = QtWidgets.QPushButton(self.centralwidget)
        self.btnClr.setObjectName("btnClr")
        self.horizontalLayout.addWidget(self.btnClr)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSpeak.clicked.connect(self.handleButton)

        self.comboMic.addItems(SpeechCls.Speech().mic_lists())
        self.comboMic.activated.connect(self.handleComboMic)
        
        self.comboLng.activated.connect(self.handleComboLang)
        
        self.btnClr.clicked.connect(self.handleBtnClear)
        
        self.btnRefresh.clicked.connect(self.refresh)
        
        self.btnAdd.clicked.connect(self.frmAdd)
        
        self.speechThread = SpeechThread()
        
        global cls
        cls = Communicate()

        self.conn = DbConnection
        self.conn.createConnection()

        cls.processSignal.connect(self.process)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "دستیار صدا"))
        self.label.setText(_translate("MainWindow", "لیست میکروفن ها"))
        self.comboLng.setItemText(0, _translate("MainWindow", "فارسی"))
        self.comboLng.setItemText(1, _translate("MainWindow", "انگلیسی"))
        self.comboLng.setItemText(2, _translate("MainWindow", "اسپانیایی"))
        self.comboLng.setItemText(3, _translate("MainWindow", "عربی"))
        self.comboLng.setItemText(4, _translate("MainWindow", "ترکی"))
        self.label_3.setText(_translate("MainWindow", "لیست زبان های موجود"))
        self.label_2.setText(_translate("MainWindow", "برای صحبت کردن  کلیک کنید"))
        self.btnSpeak.setText(_translate("MainWindow", ""))
        self.btnClr.setText(_translate("MainWindow", "پاک کردن متن"))
        self.btnAdd.setText(_translate("MainWindow", "افزودن دستورات"))
        self.btnRefresh.setText(_translate("MainWindow", "بازنشانی"))
    
    def frmAdd(self):
        dialog = QDialog()
        dialog.ui = Ui_frmAdd()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()
    
    def refresh(self):
        self.textVoice.clear()
        self.btnSpeak.setEnabled(True)
        self.speechThread.exit()

    def handleButton(self):
        self.textVoice.setText("در حال پردازش منتظر بمانید.....")
        self.btnSpeak.setEnabled(False)
        self.speechThread.start()



        
    def process(self):
        self.textVoice.clear()
        self.textVoice.setText(self.speechThread.returnText() )
        self.dbProcess()
        self.btnSpeak.setEnabled(True)
        
    def dbProcess(self):
        self.cellName = self.textVoice.toPlainText()
        if "error" in self.cellName:
            self.textVoice.setText(self.cellName)
            return
        qry = QtSql.QSqlQuery()

        qry.prepare("select * from commandRec where name = ?")
        qry.addBindValue(self.cellName)
        if(qry.exec()):
            while(qry.next()):

                cell2 = qry.value(2)
                self.cell3 = qry.value(3)
            try:    
                if(self.cell3 == "win")  :  
                  
                    try:
                        os.startfile(cell2)
                    except:
                        pass
                elif(self.cell3 == "web"):
                    try:
                        url = cell2
    #                     firefox = webbrowser.get("C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s")
    #                     firefox.open_new_tab(url)
                        webbrowser.open_new_tab(url)
                    except:
                        pass   
            except:
                self.textVoice.setText("دستور ({}) پیدا نشد.دستور را وارد کنید.".format(self.cellName))
 
    def handleComboMic(self):
        
        SpeechCls.Speech().SetMicName(str(self.comboMic.currentText()))
        
    def handleComboLang(self):
        SpeechCls.Speech().setLang(self.comboLng.currentIndex())

    def handleBtnClear(self):
        self.textVoice.clear()

class SpeechThread(QtCore.QThread):
    
    def __init__(self,parent=None):
        super(SpeechThread,self).__init__(parent)
        
    def run(self):
        self.speechText = SpeechCls.Speech().textReturn()
        cls.processSignal.emit()
        self.returnText()
    def returnText(self):
#         print(self.speechText +  "     From Button Function")
        return self.speechText
                
        
    
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
