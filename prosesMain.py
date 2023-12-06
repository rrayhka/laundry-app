from PyQt6 import QtCore, QtWidgets
from proses import Ui_Form
import sqlite3

class ProsesApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Koneksi ke database
        self.conn = sqlite3.connect('laundry.db')  # Ganti dengan nama database Anda
        self.cursor = self.conn.cursor()

        self.populateTable()  # Panggil fungsi untuk mengisi tabel saat aplikasi dimulai

    def populateTable(self):
        try:
            # Ambil data dari tabel 'proses'
            query = "SELECT * FROM proses"
            self.cursor.execute(query)
            data = self.cursor.fetchall()

            # Buat model untuk menampilkan data dalam tabel
            model = QtCore.QStandardItemModel()
            model.setColumnCount(len(data[0]))
            model.setRowCount(len(data))

            # Isi model dengan data
            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    item = QtCore.QStandardItem(str(col_data))
                    model.setItem(row_num, col_num, item)

            # Tampilkan model di QTableView
            self.ui.tableView.setModel(model)

        except sqlite3.Error as e:
            # Tangani kesalahan koneksi/database
            print("Error:", str(e))

    def closeEvent(self, event):
        # Tutup kursor dan koneksi saat form ditutup
        self.cursor.close()
        self.conn.close()

def main():
    app = QtWidgets.QApplication([])
    window = ProsesApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
