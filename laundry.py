import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

class Laundry(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect("laundry.db")
        self.db.execute("CREATE TABLE IF NOT EXISTS laundry (id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT, berat REAL, harga REAL, tanggal DATE)")
        self.db.commit()
        self.initUI()

    def initUI(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.setGeometry(200, 200, 340, 300)
        self.setWindowTitle("Aplikasi Laundry")

        # Stylesheet
        style = """
            QLabel {
                color: black;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;
                margin: 4px 2px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #45a7ca;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #45a7ca;
                border-radius: 3px;
                padding: 2px;
            }
            QTableView {
                background-color: white;
            }
        """

        self.setStyleSheet(style)

        self.formLayout = QtWidgets.QFormLayout()

        self.labelNama = QtWidgets.QLabel("Nama")
        self.labelBerat = QtWidgets.QLabel("Berat")
        self.labelHarga = QtWidgets.QLabel("Harga")
        self.labelTanggal = QtWidgets.QLabel("Tanggal")

        self.editNama = QtWidgets.QLineEdit()
        self.editBerat = QtWidgets.QLineEdit()
        self.editHarga = QtWidgets.QLineEdit()
        self.editTanggal = QtWidgets.QLineEdit()

        self.formLayout.addRow(self.labelNama, self.editNama)
        self.formLayout.addRow(self.labelBerat, self.editBerat)
        self.formLayout.addRow(self.labelHarga, self.editHarga)
        self.formLayout.addRow(self.labelTanggal, self.editTanggal)

        self.buttonTambah = QtWidgets.QPushButton("Tambah")
        self.buttonTambah.clicked.connect(self.tambahData)

        self.buttonHapus = QtWidgets.QPushButton("Hapus")
        self.buttonHapus.clicked.connect(self.hapusData)

        self.buttonUbah = QtWidgets.QPushButton("Ubah")
        self.buttonUbah.clicked.connect(self.ubahData)

        self.buttonRefresh = QtWidgets.QPushButton("Refresh")
        self.buttonRefresh.clicked.connect(self.refreshTableView)

        self.formLayout.addRow(self.buttonTambah)
        self.formLayout.addRow(self.buttonHapus)
        self.formLayout.addRow(self.buttonUbah)
        self.formLayout.addRow(self.buttonRefresh)

        self.mainLayout.addLayout(self.formLayout)

        self.tableView = QtWidgets.QTableView()
        self.mainLayout.addWidget(self.tableView)
        self.refreshTableView()

    def refreshTableView(self):
        query = self.db.execute("SELECT * FROM laundry")
        columnHeaders = [description[0] for description in query.description]
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(columnHeaders)
        for row in query:
            items = [QtGui.QStandardItem(str(item)) for item in row]
            self.model.appendRow(items)
        self.tableView.setModel(self.model)

    def tambahData(self):
        nama = self.editNama.text()
        berat = self.editBerat.text()
        harga = self.editHarga.text()
        tanggal = self.editTanggal.text()
        self.db.execute("INSERT INTO laundry (nama, berat, harga, tanggal) VALUES (?, ?, ?, ?)", (nama, berat, harga, tanggal))
        self.db.commit()
        self.refreshTableView()
        self.editNama.setText("")
        self.editBerat.setText("")
        self.editHarga.setText("")
        self.editTanggal.setText("")

    def hapusData(self):
        nama = self.editNama.text()
        self.db.execute("DELETE FROM laundry WHERE nama=?", (nama,))
        self.db.commit()
        self.refreshTableView()
        self.editNama.setText("")
        self.editBerat.setText("")
        self.editHarga.setText("")
        self.editTanggal.setText("")

    def ubahData(self):
        nama = self.editNama.text()
        berat = self.editBerat.text()
        harga = self.editHarga.text()
        tanggal = self.editTanggal.text()
        self.db.execute("UPDATE laundry SET berat=?, harga=?, tanggal=? WHERE nama=?", (berat, harga, tanggal, nama))
        self.db.commit()
        self.refreshTableView()
        self.editNama.setText("")
        self.editBerat.setText("")
        self.editHarga.setText("")
        self.editTanggal.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Laundry()
    window.show()
    sys.exit(app.exec())
