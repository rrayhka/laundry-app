import sys
import os
import PyQt6.QtCore as QtCore
import PyQt6.QtGui as QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic
import sqlite3

class Transaksi(QtWidgets.QWidgets):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect("laundry.db")
        self.setupUi()
        self.refreshTableView()

    def setupUi(self):
        self.setWindowTitle("Laundry")
        self.resize(500, 500)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.labelNama = QtWidgets.QLabel("Nama")
        self.editNama = QtWidgets.QLineEdit()
        self.formLayout.addRow(self.labelNama, self.editNama)
        self.labelBerat = QtWidgets.QLabel("Berat")
        self.editBerat = QtWidgets.QLineEdit()
        self.formLayout.addRow(self.labelBerat, self.editBerat)
        self.labelHarga = QtWidgets.QLabel("Harga")
        self.editHarga = QtWidgets.QLineEdit()
        self.formLayout.addRow(self.labelHarga, self.editHarga)
        self.labelTanggal = QtWidgets.QLabel("Tanggal")
        self.editTanggal = QtWidgets.QLineEdit()
        self.formLayout.addRow(self.labelTanggal, self.editTanggal)
        self.buttonTambah = QtWidgets.QPushButton("Tambah")
        self.buttonTambah.clicked.connect(self.tambahData)
        self.formLayout.addRow(self.buttonTambah)
        self.buttonHapus = QtWidgets.QPushButton("Hapus")
        self.buttonHapus.clicked.connect(self.hapusData)
        self.formLayout.addRow(self.buttonHapus)
        self.buttonUbah = QtWidgets.QPushButton("Ubah")
        self.buttonUbah.clicked.connect(self.ubahData)
        self.formLayout.addRow(self.buttonUbah)
        self.buttonRefresh = QtWidgets.QPushButton("Refresh")
        self.buttonRefresh.clicked.connect(self.refreshTableView)
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
        self.db.execute("INSERT INTO Laundry (nama, berat, harga, tanggal) VALUES (?, ?, ?, ?)", (nama, berat, harga, tanggal))
        self.db.commit()
        self.refreshTableView()
        self.editNama.setText("")
        self.editBerat.setText("")
        self.editHarga.setText("")
        self.editTanggal.setText("")

    def hapusData(self):
        nama = self.editNama.text()
        self.db.execute("DELETE FROM Laundry WHERE nama=?", (nama,))
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
        self.db.execute("UPDATE Laundry SET berat=?, harga=?, tanggal=? WHERE nama=?", (berat, harga, tanggal, nama))
        self.db.commit()
        self.refreshTableView()
        self.editNama.setText("")
        self.editBerat.setText("")
        self.editHarga.setText("")
        self.editTanggal.setText("")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Transaksi()
    window.show()
    sys.exit(app.exec())
    


