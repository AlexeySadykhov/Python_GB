import db_manipulation as db
from design import Ui_MainWindow
import os
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem as Twi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fill_table_view()
        self.ui.add_row_button.clicked.connect(self.add_row)
        self.ui.remove_row_button.clicked.connect(self.remove_row)
        self.ui.save_button.clicked.connect(self.save)
        self.ui.search_button.clicked.connect(self.search)
        self.ui.tableWidget.itemChanged.connect(self.on_item_changed)
        self.ui.tableWidget.model().rowsRemoved.connect(self.on_item_changed)

    def on_item_changed(self):
        self.ui.save_button.setEnabled(True)

    def set_default_table(self, headers):
        self.ui.tableWidget.setRowCount(20)
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

    def fill_table_view(self):
        path = "phonebook.db"
        headers = ["Фамилия", "Имя", "Отчество",
                   "Организация", "Мобильный телефон",
                   "Домашний телефон", "Рабочий телефон"]
        if not os.path.isfile(path):
            connection = db.connect_to_db(path)
            db.change_request(connection, db.create_query)
            self.set_default_table(headers)
        else:
            connection = db.connect_to_db(path)
            data = db.select_request(connection, "SELECT * FROM contacts;")
            if data:
                self.ui.tableWidget.setRowCount(len(data))
                self.ui.tableWidget.setColumnCount(len(data[0]))
                for i, row in enumerate(data):
                    for j, col in enumerate(row):
                        if not col:
                            continue
                        self.ui.tableWidget.setItem(i, j, Twi(str(col)))
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)
            else:
                self.set_default_table(headers)

    def add_row(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

    def remove_row(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def save(self):
        data = []
        for i in range(self.ui.tableWidget.rowCount()):
            row = []
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                if not item:
                    row.append(None)
                else:
                    row.append(item.text())
            data.append(row)
        data = list(filter(db.item_exists, data))
        connection = db.connect_to_db("phonebook.db")
        db.change_request(connection, "DELETE FROM contacts;")
        for row in data:
            db.change_request(connection, db.insert_query(row))
        self.ui.save_button.setEnabled(False)

    def search(self):
        target = self.ui.lineEdit.text().lower()
        if not target:
            QMessageBox.critical(self, "Error",
                                 "Search line is empty.",
                                 QMessageBox.Ok)
            return
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                if not item:
                    continue
                if item.text().lower().find(target) != -1:
                    self.ui.tableWidget.item(i, j).setBackground(QtGui.QColor("green"))


app = QtWidgets.QApplication(sys.argv)
application = MainWindow()
application.show()
sys.exit(app.exec_())
