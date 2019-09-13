# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets , QtSql 


class Ui_frmAdd(object):
    def setupUi(self, frmAdd):
        frmAdd.setObjectName("frmAdd")
        frmAdd.resize(512, 453)
        frmAdd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(frmAdd)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(frmAdd)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.btnRefresh = QtWidgets.QPushButton(frmAdd)
        self.btnRefresh.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.btnRefresh)
        self.groupBox = QtWidgets.QGroupBox(frmAdd)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.radioWinCmd = QtWidgets.QRadioButton(self.groupBox)
        self.radioWinCmd.setObjectName("radioWinCmd")
        self.verticalLayout_2.addWidget(self.radioWinCmd)
        self.radioWeb = QtWidgets.QRadioButton(self.groupBox)
        self.radioWeb.setObjectName("radioWeb")
        self.verticalLayout_2.addWidget(self.radioWeb)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout.addWidget(self.lineEditName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btnCommand = QtWidgets.QPushButton(self.groupBox)
        self.btnCommand.setObjectName("btnCommand")
        self.horizontalLayout_2.addWidget(self.btnCommand)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnReg = QtWidgets.QPushButton(self.groupBox)
        self.btnReg.setObjectName("btnReg")
        self.verticalLayout.addWidget(self.btnReg)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.btnCommand.clicked.connect(self.openDlg)
        self.btnReg.clicked.connect(self.register)
        self.retranslateUi(frmAdd)
        QtCore.QMetaObject.connectSlotsByName(frmAdd)
        
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.contextMenu)
        
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows);
        self.tableView.setSelectionMode( QtWidgets.QTableView.SingleSelection );

        self.tableView.doubleClicked.connect(self.editRec)
        self.btnRefresh.clicked.connect(self.refresh)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch);
        
        
        self.updateTable()
        self.filename = ""
        self.name = ""
        
        self.radioWinCmd.setChecked(True)
        
        self.btnReg.setStyleSheet("background-color:YellowGreen;font-weight:bold;font-size:25pt")

    def retranslateUi(self, frmAdd):
        _translate = QtCore.QCoreApplication.translate
        frmAdd.setWindowTitle(_translate("frmAdd", "فرم اضافه کردن دستورات"))
        self.groupBox.setTitle(_translate("frmAdd", "اضافه کردن دستورات"))
        self.label.setText(_translate("frmAdd", "نام دستور :"))
        self.btnCommand.setText(_translate("frmAdd", "انتخاب دستور"))
        self.btnReg.setText(_translate("frmAdd", "ثبت")) 
        self.btnRefresh.setText(_translate("frmAdd", "بازنشانی"))   
        self.radioWinCmd.setText(_translate("frmAdd", "دستور کامپیوتر"))
        self.radioWeb.setText(_translate("frmAdd", "اینترنت"))         
    
    def refresh(self):
        self.btnReg.disconnect()
        self.lineEditName.setText("")
        self.lineEdit.setText("") 
        self.btnReg.clicked.connect(self.register)
        self.btnReg.setText("ثبت")
        self.updateTable()
        self.btnReg.setStyleSheet("background-color:YellowGreen;font-weight:bold;font-size:25pt")
    
    def contextMenu(self,pos):
        self.menu = QtWidgets.QMenu()
        self.deleteAct = QtWidgets.QAction('حذف')
#         self.menu.addSeparator()
#         self.editAct = QtWidgets.QAction('Edit')
        self.menu.addAction(self.deleteAct)
#         self.menu.addAction(self.editAct)
        self.deleteAct.triggered.connect(self.deleteAction)
        self.menu.exec_(QtGui.QCursor.pos())

    def deleteAction(self):
        index = self.tableView.currentIndex()
        NewIndex = self.tableView.model().index(index.row(), 0)
        id = self.tableView.model().data(NewIndex)

        qry = QtSql.QSqlQuery()
        qry.prepare("delete from commandRec where ID = ?")
        qry.addBindValue(id)
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('حذف')
        msg_box.setText("آیا برای حذف مطمئن هستید؟")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        reply = msg_box.exec()
        if (reply == QtWidgets.QMessageBox.Yes):
            qry.exec();
            self.updateTable()
     
    def editRec(self):     
        index = self.tableView.currentIndex()
        indexCmd = self.tableView.model().index(index.row(), 3)
        self.cmdType = self.tableView.model().data(indexCmd)
        if(self.cmdType == "win"):
            self.radioWinCmd.setChecked(True)
        elif(self.cmdType == "web"):
            self.radioWeb.setChecked(True)
        
        
        self.btnReg.disconnect()
        self.btnReg.setText("اصلاح")
        self.btnReg.setStyleSheet("background-color:Khaki;font-weight:bold;font-size:25pt")
        self.btnReg.clicked.connect(self.editSlot)
        index = self.tableView.currentIndex()
        NewIndex = self.tableView.model().index(index.row(), 0)
        id = self.tableView.model().data(NewIndex)
        self.qry = QtSql.QSqlQuery()
        self.qry.prepare("select * from commandRec where ID = ?")
        self.qry.addBindValue(id)  

        self.qry.exec()
        while(self.qry.next()):
            cell1 = str(self.qry.value(1))
            cell2 = str(self.qry.value(2))
        self.lineEditName.setText(cell1)
        self.lineEdit.setText(cell2)
        
    
    def editSlot(self): 
        self.name = self.lineEditName.text()
        
        if(self.radioWinCmd.isChecked()):
            cmd = "win"
        elif(self.radioWeb.isChecked()):
            cmd = "web"
            
        index = self.tableView.currentIndex()
        NewIndex = self.tableView.model().index(index.row(), 0)
        id = self.tableView.model().data(NewIndex)

        self.qry.prepare("update commandRec set name= ?, command= ? , cmd=? where ID= ?")
        self.qry.addBindValue(self.lineEditName.text())
        self.qry.addBindValue(self.lineEdit.text())
        self.qry.addBindValue(cmd)
        self.qry.addBindValue(id); 
        if(self.qry.exec()):
  
            QtWidgets.QMessageBox.information(None, "اصلاح","با موفقیت  اصلاح  شد", QtWidgets.QMessageBox.Ok)  
            self.updateTable()      

        else :
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                     "Unable to establish a database connection.\n"
                     "This example needs SQLite support. Please read "
                     "the Qt SQL driver documentation for information how "
                     "to build it.\n\n"
                     "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            
        self.lineEditName.setText("")
        self.lineEdit.setText("") 
        self.btnReg.disconnect()
        self.btnReg.clicked.connect(self.register)
        self.btnReg.setText("ثبت")
        self.btnReg.setStyleSheet("background-color:YellowGreen;font-weight:bold;font-size:25pt")
        self.updateTable()
        
    def updateTable(self):
        
        model = QtSql.QSqlQueryModel()

        qry = QtSql.QSqlQuery()
    
        qry.prepare("select * from commandRec")
        if(qry.exec()):
            pass 
        else:
            QtWidgets.QMessageBox.information(None,"خطا","امکان وصل شدن به پایگاه داده وجود ندارد", QtWidgets.QMessageBox.Ok)
            self.btnReg.setEnabled(False)
            self.btnCommand.setEnabled(False)
            self.btnRefresh.setEnabled(False)
        model.setQuery(qry);
    
        self.tableView.setModel(model);
        self.tableView.hideColumn(0)
#         self.tableView.hideColumn(3)
        model.setHeaderData(1, QtCore.Qt.Horizontal, "نام دستور");
        model.setHeaderData(2, QtCore.Qt.Horizontal, "دستور");
        model.setHeaderData(3, QtCore.Qt.Horizontal, "نوع دستور");
    def openDlg(self):
        self.filename,_filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open " + "key" + " Data File", '.', "(*.*)")
        self.lineEdit.setText(str(self.filename))
        
    def register(self):
        self.name = self.lineEditName.text()
        if(self.radioWinCmd.isChecked()):
            self.cmd = "win"
        if(self.radioWeb.isChecked()):
            self.cmd = "web"
        qry = QtSql.QSqlQuery()
        if(self.lineEdit.text()!= "" ) and  (self.lineEditName.text()!= "" ):
            qry.prepare("insert into commandRec(name,command,cmd) values ('"+self.name+"','"+self.lineEdit.text()+"','"+self.cmd+"')")

    #         qry.exec()
    
            if(qry.exec()):
              
                        QtWidgets.QMessageBox.information(None, "ثبت","با موفقیت ثبت شد", QtWidgets.QMessageBox.Ok)  
                        self.updateTable()  
                        self.lineEditName.setText("")
                        self.lineEdit.setText("")     
    
            else :
                        QtWidgets.QMessageBox.critical(None,"خطا","رکورد موجود است", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(None,"خطا","دستور و نام دستور را وارد کنید", QtWidgets.QMessageBox.Ok)


  