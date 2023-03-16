from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.add_row_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_row_button.setObjectName("add_row_button")
        self.gridLayout.addWidget(self.add_row_button, 5, 1, 1, 1)
        self.remove_row_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_row_button.setEnabled(True)
        self.remove_row_button.setObjectName("remove_row_button")
        self.gridLayout.addWidget(self.remove_row_button, 6, 1, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setEnabled(False)
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 7, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phonebook manager"))
        self.add_row_button.setText(_translate("MainWindow", "Add Row"))
        self.remove_row_button.setText(_translate("MainWindow", "Remove Row"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.search_button.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
