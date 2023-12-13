from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMdiSubWindow, QMessageBox, QMainWindow, QComboBox
from PyQt6 import QtCore, QtWidgets, QtSql, QtGui


#################################### TAMPILAN HALAMAN AWAL ####################################

# class Ui_Form(object) merupakan kode hasil konvert dari file formLaundryAkh.ui
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 530)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(320, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(430, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(430, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(500, 160, 211, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(430, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(430, 220, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(500, 220, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(430, 320, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 400, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 110, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 190, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 260, 211, 191))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 110, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 270, 211, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 320, 211, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Folmulir Laundry"))
        self.label_2.setText(_translate("Form", "Nama"))
        self.label_3.setText(_translate("Form", "No Telepon"))
        self.label_4.setText(_translate("Form", "Alamat"))
        self.label_5.setText(_translate("Form", "Id Tas"))
        self.label_6.setText(_translate("Form", "Tanggal"))
        self.label_7.setText(_translate("Form", "Berat"))
        self.label_8.setText(_translate("Form", "Kategori"))
        self.comboBox.setItemText(0, _translate("Form", "Cuci Basah"))
        self.comboBox.setItemText(1, _translate("Form", "Cuci Kering"))
        self.comboBox.setItemText(2, _translate("Form", "Cuci Setrika"))
        self.comboBox.setItemText(3, _translate("Form", "Setrika"))
        self.label_9.setText(_translate("Form", "Biaya"))
        self.pushButton.setText(_translate("Form", "Kirim"))

# class form(QMdiSubWindow) merupakan kode utama agar kelas Ui_Form bisa di insert ke dalam table proses
class form(QMdiSubWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = QSqlTableModel(self)
        self.model.setTable("pembayaran")
        self.model.select()

        self.ui.pushButton.clicked.connect(self.submit)

    def submit(self):
        nama = self.ui.lineEdit.text()
        nomor = self.ui.lineEdit_2.text()
        alamat = self.ui.lineEdit_3.text()
        id_tas = self.ui.lineEdit_4.text()
        berat = self.ui.lineEdit_5.text()
        biaya = self.ui.lineEdit_6.text()
        kategori = self.ui.comboBox.currentText()
        tanggal = self.ui.dateEdit.date().toString('yyyy-MM-dd')

        query = QSqlQuery()
        query.prepare("INSERT INTO user (nama, alamat, no_tlpn) VALUES (?, ?, ?)")
        query.bindValue(0, nama)
        query.bindValue(1, alamat)
        query.bindValue(2, nomor)
        
        if not query.exec():
            QMessageBox.critical(self, "Error", "Error inserting into user table: " + query.lastError().text())
            return

        id_user = query.lastInsertId()

        query.prepare("INSERT INTO proses (id_user, id_tas, tanggal_proses, kategori, berat, total_bayar, status_proses) VALUES (?, ?, ?, ?, ?, ?, 'Proses')")
        query.bindValue(0, id_user)
        query.bindValue(1, id_tas)
        query.bindValue(2, tanggal)
        query.bindValue(3, kategori)
        query.bindValue(4, berat)
        query.bindValue(5, biaya)

        if not query.exec():
            QMessageBox.critical(self, "Error", "Error inserting into proses table: " + query.lastError().text())
            return
        
        id_proses = query.lastInsertId()
        query.prepare("INSERT INTO pembayaran (id_proses, jumlah_bayar, metode_bayar, tanggal_bayar) VALUES (?, ?, 'Cash', CURRENT_DATE)")
        query.bindValue(0, id_proses)
        query.bindValue(1, biaya)

        if not query.exec():
            QMessageBox.critical(self, "Error", "Error inserting into pembayaran table: " + query.lastError().text())
            return

        self.model.select()

#################################### TAMPILAN TABLE PROSES ####################################

# kelas Ui_EditProses merupakan hasil konvert dari editProses.ui
class Ui_EditProses(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 336)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(40, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 120, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 170, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 220, 111, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 280, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 280, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 280, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(190, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(270, 70, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 70, 111, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(270, 120, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 120, 111, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(270, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 170, 111, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(270, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(360, 220, 111, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Id Proses"))
        self.label_2.setText(_translate("Form", "Id User"))
        self.label_3.setText(_translate("Form", "Id Tas"))
        self.label_4.setText(_translate("Form", "Tanggal Proses"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Sebelumnya"))
        self.pushButton_3.setText(_translate("Form", "Selanjutnya"))
        self.label_9.setText(_translate("Form", "Edit Proses"))
        self.label_5.setText(_translate("Form", "Kategori"))
        self.label_6.setText(_translate("Form", "Berat"))
        self.label_7.setText(_translate("Form", "Total Bayar"))
        self.label_8.setText(_translate("Form", "Status Proses"))
# kelas editProses terdapat logic untuk mengedit data di table proses dengan tampilan yang didapat dari kelas Ui_EditProses
class editProses(QMdiSubWindow):
    def __init__(self, row, model, parent=None):
        super().__init__(parent)
        self.ui = Ui_EditProses()
        self.ui.setupUi(self)
        self.current_row = row
        self.model = model
        self.lineEdit = self.ui.lineEdit
        self.lineEdit_2 = self.ui.lineEdit_2
        self.lineEdit_3 = self.ui.lineEdit_3
        self.lineEdit_4 = self.ui.lineEdit_4
        self.lineEdit_5 = self.ui.lineEdit_5
        self.lineEdit_6 = self.ui.lineEdit_6
        self.lineEdit_7 = self.ui.lineEdit_7
        self.lineEdit_8 = self.ui.lineEdit_8
        self.pushButton = self.ui.pushButton

        self.displayRec()
        self.ui.pushButton_2.clicked.connect(self.dispPrevious)
        self.ui.pushButton_3.clicked.connect(self.dispNext)
        self.pushButton.clicked.connect(self.saveRecord)

    def displayRec(self):
        self.record_dict = {}
        for i in range(self.model.rowCount()):
            self.model.record(i)
            self.record_dict[i] = {
                "id_proses": self.model.data(self.model.index(i, 0)),
                "id_user": self.model.data(self.model.index(i, 1)),
                "id_tas": self.model.data(self.model.index(i, 2)),
                "tgl_proses": self.model.data(self.model.index(i, 3)),
                "kategori": self.model.data(self.model.index(i, 4)),
                "berat": self.model.data(self.model.index(i, 5)),
                "total_bayar": self.model.data(self.model.index(i, 6)),
                "status_proses": self.model.data(self.model.index(i, 7)),
            }

        self.display_current_record()

    def display_current_record(self):
        current_record = self.record_dict.get(self.current_row)
        if current_record:
            self.lineEdit.setText(str(current_record["id_proses"]))
            self.lineEdit_2.setText(str(current_record["id_user"]))
            self.lineEdit_3.setText(str(current_record["id_tas"]))
            self.lineEdit_4.setText(str(current_record["tgl_proses"]))
            self.lineEdit_5.setText(str(current_record["kategori"]))
            self.lineEdit_6.setText(str(current_record["berat"]))
            self.lineEdit_7.setText(str(current_record["total_bayar"]))
            self.lineEdit_8.setText(str(current_record["status_proses"]))


    def saveRecord(self):
        id_proses = self.lineEdit.text()
        id_user = self.lineEdit_2.text()
        id_tas = self.lineEdit_3.text()
        tgl_proses = self.lineEdit_4.text()
        kategori = self.lineEdit_5.text()
        berat = self.lineEdit_6.text()
        total_bayar = self.lineEdit_7.text()
        status_proses = self.lineEdit_8.text()

        query = QSqlQuery()
        query.prepare("""
            UPDATE proses 
            SET 
            id_user = :id_user,
            id_tas = :id_tas,
            tanggal_proses = :tgl_proses,
            kategori = :kategori,
            berat = :berat,
            total_bayar = :total_bayar,
            status_proses = :status_proses
            WHERE id_proses = :id_proses
        """)

        query.bindValue(':id_user', id_user)
        query.bindValue(':id_tas', id_tas)
        query.bindValue(':tgl_proses', tgl_proses)
        query.bindValue(':kategori', kategori)
        query.bindValue(':berat', berat)
        query.bindValue(':total_bayar', total_bayar)
        query.bindValue(':status_proses', status_proses)
        query.bindValue(':id_proses', id_proses)

        if query.exec():
            self.model.setQuery(QSqlQuery("SELECT * FROM proses"))
            self.displayRec()
            print("Record updated successfully.")
        else:
            print("Error:", query.lastError().text())


    def dispPrevious(self):
        if self.current_row > 0:
            self.current_row -= 1
            self.displayRec()

    def dispNext(self):
        if self.current_row < self.model.rowCount() - 1:
            self.current_row += 1
            self.displayRec()


# kelas Ui_AddProses merupakan hasil konvert dari file addProses.ui 
class Ui_AddProses(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 270)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 120, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(120, 170, 111, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 220, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(190, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(270, 70, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(270, 120, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 120, 111, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(270, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 170, 111, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_2.setGeometry(QtCore.QRect(360, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Id User"))
        self.label_3.setText(_translate("Form", "Id Tas"))
        self.label_4.setText(_translate("Form", "Tanggal Proses"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label_9.setText(_translate("Form", "Add Proses"))
        self.label_5.setText(_translate("Form", "Kategori"))
        self.label_6.setText(_translate("Form", "Berat"))
        self.label_7.setText(_translate("Form", "Total Bayar"))
        self.label_8.setText(_translate("Form", "Status Proses"))
        self.comboBox.setItemText(0, _translate("Form", "New Item"))
        self.comboBox_2.setItemText(0, _translate("Form", "Cuci Kering"))
        self.comboBox_2.setItemText(1, _translate("Form", "Cuci Basah"))
        self.comboBox_2.setItemText(2, _translate("Form", "Cuci Setrika"))
        self.comboBox_2.setItemText(3, _translate("Form", "Setrika"))
        self.comboBox_3.setItemText(0, _translate("Form", "Proses"))
        self.comboBox_3.setItemText(1, _translate("Form", "Selesai"))

# addProses merupakan logic untuk menambahkan data ke database dengan tampilan yang didapat dari kelas Ui_AddProses
class addProses(QMdiSubWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProses()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.saveRecord)

        self.populateComboBox()  # Panggil fungsi untuk mengisi comboBox

    def populateComboBox(self):
        query = QSqlQuery()
        if query.exec("SELECT id_user FROM proses"):  # Ganti query sesuai kebutuhan Anda
            self.ui.comboBox.clear()  # Bersihkan comboBox sebelum mengisi ulang
            while query.next():
                id_user = query.value(0)  # Ambil nilai id_user dari query
                self.ui.comboBox.addItem(str(id_user))  # Tambahkan nilai ke comboBox
        else:
            print("Failed to fetch id_user:", query.lastError().text())

    def saveRecord(self):
        id_user = self.ui.comboBox.currentText()
        id_tas = self.ui.lineEdit_3.text()
        tgl_proses = self.ui.dateEdit.date().toString('yyyy-MM-dd')
        kategori = self.ui.comboBox_2.currentText()
        berat = self.ui.lineEdit_6.text()
        total_bayar = self.ui.lineEdit_7.text()
        status_proses = self.ui.comboBox_3.currentText()

        query = QSqlQuery()
        query.exec(f"INSERT INTO proses (id_user, id_tas, tanggal_proses, kategori, berat, total_bayar, status_proses) VALUES ('{id_user}', '{id_tas}', '{tgl_proses}', '{kategori}', '{berat}', '{total_bayar}', '{status_proses}')")
        if query.lastError().isValid():
            print("Error:", query.lastError().text())
        else:
            print("Record inserted successfully.")
            self.close()


# kelas Ui_Proses berfungsi sebagai tampilan utama dari proses yang merupakan hasil konvert dari file proses.ui
class Ui_Proses(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(787, 527)
        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 430, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 90, 91, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(690, 90, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 430, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 430, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 430, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 90, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(180, 90, 51, 31))
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(parent=Form)
        self.tableView.setGeometry(QtCore.QRect(60, 150, 681, 261))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(350, 90, 51, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 90, 91, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(510, 90, 51, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(560, 90, 101, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_6.setText(_translate("Form", "Tambah"))
        self.pushButton.setText(_translate("Form", "Cari"))
        self.pushButton_3.setText(_translate("Form", "Delete"))
        self.pushButton_4.setText(_translate("Form", "Update All"))
        self.pushButton_5.setText(_translate("Form", "Edit"))
        self.label_2.setText(_translate("Form", "Id User"))
        self.label.setText(_translate("Form", "Id Proses"))
        self.label_3.setText(_translate("Form", "Kategori"))
        self.label_4.setText(_translate("Form", "Status"))
# kelas proses merupakan logic untuk menampilkan data dari database dengan tampilan yang didapat dari kelas Ui_Proses
class proses(QMdiSubWindow):
    def __init__(self, parent=None):
        super(proses, self).__init__(parent)
        self.ui = Ui_Proses()
        self.ui.setupUi(self)
        self.model = QSqlTableModel(self)
        self.model.setTable('proses')
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)

        self.ui.pushButton.clicked.connect(self.cari)
        self.ui.pushButton_5.clicked.connect(self.edit)
        self.ui.pushButton_4.clicked.connect(self.update)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_6.clicked.connect(self.tambah)

    def cari(self):
        filter1 = self.ui.lineEdit.text()
        filter2 = self.ui.lineEdit_2.text()
        filter3 = self.ui.lineEdit_3.text()
        filter4 = self.ui.lineEdit_4.text()

        if filter1 == "" and filter2 == "" and filter3 == "" and filter4 == "":
            self.model.setFilter("")
        else:
            self.model.setFilter(f"id_proses LIKE '%{filter1}%' AND id_user LIKE '%{filter2}%' AND kategori LIKE '%{filter3}%' AND status_proses LIKE '%{filter4}%'")

    def tambah(self):
        self.add = addProses()
        self.add.show()

    def edit(self):
        row = self.ui.tableView.currentIndex().row()
        self.edit = editProses(row, self.model)
        self.edit.show()

    def delete(self):
        row = self.ui.tableView.currentIndex().row()
        self.model.removeRow(row)
        self.model.submitAll()

    def update(self):
        self.model.submitAll()
        self.model.select()


#################################### TAMPILAN TABLE PEMBAYARAN  ####################################

# kelas Ui_EditPembayaran merupakan hasil konvert dari file editPembayaran.ui
class Ui_EditPembayaran(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 424)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(70, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 140, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 190, 161, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(70, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 290, 161, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 370, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 370, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(150, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ID Pembayaran"))
        self.label_2.setText(_translate("Form", "ID Proses"))
        self.label_3.setText(_translate("Form", "Jumlah Bayar"))
        self.label_4.setText(_translate("Form", "Metode Bayar"))
        self.label_5.setText(_translate("Form", "Tanggal Bayar"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Sebelumnya"))
        self.pushButton_3.setText(_translate("Form", "Selanjutnya"))
        self.label_6.setText(_translate("Form", "Folmulir Pembayaran"))
        self.comboBox.setItemText(0, _translate("Form", "Cash"))
        self.comboBox.setItemText(1, _translate("Form", "Kredit"))
# kelas editPembayaran di dalamnya terdapat logic untuk mengedit data di table pembayaran
class editPembayaran(QMdiSubWindow):
    def __init__(self, row, model, parent=None):
        super().__init__(parent)
        self.ui = Ui_EditPembayaran()
        self.ui.setupUi(self)
        self.current_row = row
        self.model = model

        self.lineEdit = self.ui.lineEdit
        self.lineEdit_2 = self.ui.lineEdit_2
        self.lineEdit_3 = self.ui.lineEdit_3
        self.lineEdit_5 = self.ui.lineEdit_5
        self.comboBox = self.ui.comboBox

        self.displayRec()

        self.ui.pushButton_2.clicked.connect(self.dispPrevious)
        self.ui.pushButton_3.clicked.connect(self.dispNext)
        self.ui.pushButton.clicked.connect(self.saveRecord) 

    def displayRec(self):
        self.record_dict = {}
        for i in range(self.model.rowCount()):
            self.model.record(i)
            self.record_dict[i] = {
                "id_bayar": self.model.data(self.model.index(i, 0)),
                "id_proses": self.model.data(self.model.index(i, 1)),
                "jumlah_bayar": self.model.data(self.model.index(i, 2)),
                "metode_bayar": self.model.data(self.model.index(i, 3)),
                "tanggal_bayar": self.model.data(self.model.index(i, 4)),
            }

        self.display_current_record()
    
    def display_current_record(self):
        current_record = self.record_dict.get(self.current_row)
        if current_record:
            self.lineEdit.setText(str(current_record["id_bayar"]))
            self.lineEdit_2.setText(str(current_record["id_proses"]))
            self.lineEdit_3.setText(str(current_record["jumlah_bayar"]))
            self.lineEdit_5.setText(str(current_record["tanggal_bayar"]))
            tanggal_bayar_str = current_record["tanggal_bayar"]
            tanggal_bayar_qdate = QtCore.QDate.fromString(tanggal_bayar_str, "yyyy-MM-dd")


    def dispPrevious(self):
        if self.current_row > 0:
            self.current_row -= 1
            self.display_current_record()

    def dispNext(self):
        if self.current_row < len(self.record_dict) - 1:
            self.current_row += 1
            self.display_current_record()
    def saveRecord(self):
        id_bayar = self.lineEdit.text()
        id_proses = self.lineEdit_2.text()
        jumlah_bayar = self.lineEdit_3.text()
        metode_bayar = self.comboBox.currentText()
        tanggal_bayar = self.lineEdit_5.text()

        query = QSqlQuery()
        query.prepare("""
            UPDATE pembayaran 
            SET 
            id_proses = :id_proses,
            jumlah_bayar = :jumlah_bayar,
            metode_bayar = :metode_bayar,
            tanggal_bayar = :tanggal_bayar
            WHERE id_pembayaran = :id_bayar
        """)
        
        query.bindValue(':id_proses', id_proses)
        query.bindValue(':jumlah_bayar', jumlah_bayar)
        query.bindValue(':metode_bayar', metode_bayar)
        query.bindValue(':tanggal_bayar', tanggal_bayar)
        query.bindValue(':id_bayar', id_bayar)

        if query.exec():
            self.model.setQuery(QSqlQuery("SELECT * FROM pembayaran"))
            self.displayRec()
        else:
            print("Gagal menyimpan data")  # Atau handle kesalahan dengan cara lain sesuai kebutuhan
        pass


# kelas Ui_addPembayaran merupakan hasil konvert dari file addPembayaran.ui
class Ui_addPembayaran(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 432)
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        # self.pushButton_3 = QtWidgets.QPushButton(Form)
        # self.pushButton_3.setGeometry(QtCore.QRect(370, 370, 75, 23))
        # self.pushButton_3.setObjectName("pushButton_3")
        
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(240, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Cash")
        self.comboBox.addItem("Kredit")
        
        # self.pushButton_2 = QtWidgets.QPushButton(Form)
        # self.pushButton_2.setGeometry(QtCore.QRect(70, 370, 75, 23))
        # self.pushButton_2.setObjectName("pushButton_2")
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 190, 161, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(240, 290, 161, 31))  # Ubah posisi dan ukuran dateEdit
        self.dateEdit.setObjectName("dateEdit")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 140, 161, 31))  # Ubah posisi dan ukuran comboBox_2
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "ID Proses"))
        # self.pushButton_3.setText(_translate("Form", "Selanjutnya"))
        self.label_5.setText(_translate("Form", "Tanggal Bayar"))
        self.label_6.setText(_translate("Form", "Add Pembayaran"))
        # self.pushButton_2.setText(_translate("Form", "Sebelumnya"))
        self.label_3.setText(_translate("Form", "Jumlah Bayar"))
        self.label_4.setText(_translate("Form", "Metode Bayar"))
        self.pushButton.setText(_translate("Form", "Save"))
        # Memanggil fungsi untuk mengisi comboBox_2 dengan ID Proses
        self.populateProsesComboBox()

    def populateProsesComboBox(self):  # Ubah dari self,comboBox_2 menjadi self saja
        query = QtSql.QSqlQuery()
        id_proses_list = []
        
        if query.exec("SELECT id_proses FROM proses"):
            while query.next():
                id_proses = query.value(0)
                id_proses_list.append(id_proses)
            
            self.comboBox_2.addItems([str(item) for item in id_proses_list])

        else:
            print("Error:", query.lastError().text())

class addPembayaran(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addPembayaran()
        self.ui.setupUi(self)

        self.ui.populateProsesComboBox()  # Memanggil fungsi untuk mengisi comboBox_2 dengan ID Proses

        self.ui.pushButton.clicked.connect(self.saveRecord)

    def saveRecord(self):
        id_proses = self.ui.comboBox_2.currentText()  # Mengambil ID Proses yang dipilih dari combo box
        jumlah_bayar = self.ui.lineEdit_3.text()  # Mengambil jumlah bayar dari QLineEdit
        metode_bayar = self.ui.comboBox.currentText()  # Mengambil metode bayar dari combo box
        tanggal_bayar = self.ui.dateEdit.date().toString('yyyy-MM-dd')  # Mengambil tanggal bayar dari QLineEdit

        query = QtSql.QSqlQuery()
        query.prepare("INSERT INTO pembayaran (id_proses, jumlah_bayar, metode_bayar, tanggal_bayar) " 
                    "VALUES (:id_proses, :jumlah_bayar, :metode_bayar, :tanggal_bayar)")
        query.bindValue(":id_proses", id_proses)
        query.bindValue(":jumlah_bayar", jumlah_bayar)
        query.bindValue(":metode_bayar", metode_bayar)
        query.bindValue(":tanggal_bayar", tanggal_bayar)

        if not query.exec():
            print("Error:", query.lastError().text())
        else:
            print("Record inserted successfully.")
            self.close()
# kelas Ui_Pembayaran merupakan hasil konvert dari file pembayaranMain.ui
class Ui_Pembayaran(object):
    def setupUi(self, Form):
        Form.setObjectName("Pembayaran")
        Form.resize(784, 528)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 80, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 420, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(50, 80, 81, 31))
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(parent=Form)
        self.tableView.setGeometry(QtCore.QRect(50, 140, 681, 261))
        self.tableView.setObjectName("tableView")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 420, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 420, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 420, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 80, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(340, 80, 81, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Cari"))
        self.pushButton_3.setText(_translate("Form", "Delete"))
        self.label.setText(_translate("Form", "Id Pembayaran"))
        self.pushButton_4.setText(_translate("Form", "Update All"))
        self.pushButton_5.setText(_translate("Form", "Edit"))
        self.pushButton_6.setText(_translate("Form", "Tambah"))
        self.label_2.setText(_translate("Form", "Tanggal Bayar"))
# kelas pembayaran terdapat logic untuk menampilkan data pembayaran, edit data pembayaran, delete data pembayaran, filter data pembayaran, menambahkan data pembayaran
class pembayaran(QMdiSubWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pembayaran()
        self.ui.setupUi(self)
        self.model = QSqlTableModel(self)
        self.model.setTable('pembayaran')
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.pushButton_5.clicked.connect(self.editRecord)
        self.ui.pushButton_3.clicked.connect(self.deleteRecord)
        self.ui.pushButton.clicked.connect(self.filterRecord)
        self.ui.pushButton_4.clicked.connect(self.updateAll)
        self.ui.pushButton_6.clicked.connect(self.addRecord)

    def editRecord(self):
        row = self.ui.tableView.currentIndex().row()
        self.edit = editPembayaran(row, self.model)
        self.edit.show()  


    def deleteRecord(self):
        row = self.ui.tableView.currentIndex().row()
        self.model.removeRow(row)
        self.model.submitAll()

    def filterRecord(self):
        filter_value1 = self.ui.lineEdit.text()  
        filter_value2 = self.ui.lineEdit_2.text() 

        self.model.setFilter(f"id_pembayaran LIKE '%{filter_value1}%' OR metode_bayar LIKE '%{filter_value2}%'")
        self.model.select()

    def updateAll(self):
        self.model.submitAll()

    def addRecord(self):
        self.add = addPembayaran()
        self.add.show()



#################################### KODE UNTUK MAIN  ####################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 570)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(parent=self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 831, 551))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        self.menuFormulir_Laundry = QtWidgets.QMenu(parent=self.menubar)
        self.menuFormulir_Laundry.setObjectName("menuFormulir_Laundry")
        self.menuProses = QtWidgets.QMenu(parent=self.menubar)
        self.menuProses.setObjectName("menuProses")
        self.menuPembayaran = QtWidgets.QMenu(parent=self.menubar)
        self.menuPembayaran.setObjectName("menuPembayaran")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFormulir_Laundry.menuAction())
        self.menubar.addAction(self.menuProses.menuAction())
        self.menubar.addAction(self.menuPembayaran.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.koneksi()
        self.show()
        self.ui.menuFormulir_Laundry.triggered.connect(lambda: self.show_content(0))
        self.ui.menuProses.triggered.connect(lambda: self.show_content(1))
        self.ui.menuPembayaran.triggered.connect(lambda: self.show_content(2))

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.form_window = form()
        self.proses_window = proses()
        self.pembayaran_window = pembayaran()

        self.tab_widget.addTab(self.form_window, "Formulir Laundry")
        self.tab_widget.addTab(self.proses_window, "Proses")
        self.tab_widget.addTab(self.pembayaran_window, "Pembayaran")

        # # Panggil fungsi tambah_data() setelah koneksi berhasil
        # self.koneksi_berhasil.connect(self.tambah_data)

    koneksi_berhasil = QtCore.pyqtSignal()

    def koneksi(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('laundry.db')
        if not db.open():
            self.statusBar().showMessage("Galat !! Database connection failed")
        else:
            self.statusBar().showMessage("Koneksi database berhasil")
            self.tables()
            self.koneksi_berhasil.emit()

    def tables(self):
        query = QSqlQuery()
        query.exec("""
            CREATE TABLE IF NOT EXISTS "user" (
                "id_user" INTEGER PRIMARY KEY AUTOINCREMENT,
                "nama" VARCHAR(20) NOT NULL,
                "alamat" VARCHAR(50) NOT NULL,
                "no_tlpn" VARCHAR(15) NOT NULL
            )
        """)
        query.exec("""
            CREATE TABLE IF NOT EXISTS "proses" (
                "id_proses" INTEGER PRIMARY KEY AUTOINCREMENT,
                "id_user" int NOT NULL,
                "id_tas" int NOT NULL,
                "tanggal_proses" DATE NOT NULL,
                "kategori" VARCHAR(100) NOT NULL,
                "berat" VARCHAR(20) NOT NULL,
                "total_bayar" FLOAT NOT NULL,
                "status_proses" VARCHAR(50) NOT NULL,
                FOREIGN KEY("id_user") REFERENCES "user"("id_user")
            )
        """)
        query.exec("""
            CREATE TABLE IF NOT EXISTS "pembayaran" (
                "id_pembayaran" INTEGER PRIMARY KEY AUTOINCREMENT,
                "id_proses" int NOT NULL,
                "jumlah_bayar" int NOT NULL,
                "metode_bayar" VARCHAR(50) NOT NULL,
                "tanggal_bayar" DATETIME NOT NULL,
                FOREIGN KEY("id_proses") REFERENCES "proses"("id_proses")
            )
        """)
    def show_content(self, index):
        self.tab_widget.setCurrentIndex(index)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = main()
    sys.exit(app.exec())