from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(787, 527)
        self.tableView = QtWidgets.QTableView(parent=Form)
        self.tableView.setGeometry(QtCore.QRect(60, 80, 681, 261))
        self.tableView.setObjectName("tableView")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(460, 20, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 20, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(380, 20, 61, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 360, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 360, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 360, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Cari"))
        self.label.setText(_translate("Form", "Searching"))
        self.pushButton_2.setText(_translate("Form", "Sebelumnya"))
        self.pushButton_3.setText(_translate("Form", "Selanjutnya"))
        self.pushButton_4.setText(_translate("Form", "Update All"))


class ProsesApp(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("laundry.db")
        self.db.open()
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("proses")
        # self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.pushButton.clicked.connect(self.FilterRecord)
        # self.ui.pushButton_2.clicked.connect(self.previousRecord)
        # self.ui.pushButton_3.clicked.connect(self.nextRecord)
        self.ui.pushButton_4.clicked.connect(self.updateAll)


    def updateAll(self):
        self.model.submitAll()

    def FilterRecord(self):
        filter_value = self.ui.lineEdit.text()
        self.model.setFilter(f"id_proses LIKE '%{filter_value}%' OR id_user LIKE '%{filter_value}%' OR id_tas LIKE '%{filter_value}%' OR tanggal_proses LIKE '%{filter_value}%' OR kategori LIKE '%{filter_value}%' OR berat LIKE '%{filter_value}%' OR total_bayar LIKE '%{filter_value}%' or status_proses LIKE '%{filter_value}%'")





def main():
    app = QtWidgets.QApplication([])
    window = ProsesApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
