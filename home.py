from PyQt5 import QtWidgets,QtCore
class MyObject(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(50, 50, 140, 20))
        self.label_A.setObjectName("label_A")
        self.input_A = QtWidgets.QLineEdit(self.centralwidget)
        self.input_A.setGeometry(QtCore.QRect(180, 50, 100, 20))
        self.input_A.setObjectName("input_A")
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(50, 80, 140, 20))
        self.label_B.setObjectName("label_B")
        self.input_B = QtWidgets.QLineEdit(self.centralwidget)
        self.input_B.setGeometry(QtCore.QRect(180, 80, 100, 20))
        self.input_B.setObjectName("input_B")
        self.label_C = QtWidgets.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(50, 110, 140, 20))
        self.label_C.setObjectName("label_C")
        self.input_C = QtWidgets.QLineEdit(self.centralwidget)
        self.input_C.setGeometry(QtCore.QRect(180, 110, 100, 20))
        self.input_C.setObjectName("input_C")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(130, 180, 100, 30))
        self.calculate_button.setObjectName("calculate_button")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(150, 150, 100, 20))
        self.result_label.setObjectName("result_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tính S"))
        self.label_A.setText(_translate("MainWindow", "Nhập số vốn ban đầu:"))
        self.label_B.setText(_translate("MainWindow", "Nhập số % lãi suất"))
        self.label_C.setText(_translate("MainWindow", "Nhập số kỳ hạn"))
        self.calculate_button.setText(_translate("MainWindow", "Tính"))
        self.result_label.setText(_translate("MainWindow", "S = "))

        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        A = float(self.input_A.text())
        r = float(self.input_B.text())
        n = float(self.input_C.text())
        S = A * (1 + n * r/100)
        self.result_label.setText("S = " + str(S))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    home = QtWidgets.QMainWindow()
    ui = MyObject()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())