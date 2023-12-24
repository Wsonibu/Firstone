
from PyQt5 import QtGui,QtWidgets,QtCore
from SW import Ui_SW
class Ui_home(object):
    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_SW()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.P1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.P1.setGeometry(QtCore.QRect(100, 210, 261, 61))
        self.P1.setObjectName("P1")
        self.P2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.P2.setGeometry(QtCore.QRect(100, 300, 261, 61))
        self.P2.setObjectName("P2")
        self.P3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.P3.setGeometry(QtCore.QRect(240, 390, 331, 61))
        self.P3.setObjectName("P3")
        self.P4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.P4.setGeometry(QtCore.QRect(240, 470, 331, 61))
        self.P4.setObjectName("P4")
        self.P5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.P5.setGeometry(QtCore.QRect(460, 210, 271, 61))
        self.P5.setObjectName("P5")
        self.P6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.P6.setGeometry(QtCore.QRect(460, 300, 271, 61))
        self.P6.setObjectName("P6")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 50, 800, 100))
        self.label1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(320, 90, 780, 120))

        self.P1.clicked.connect(self.openwindow)
        self.P1.clicked.connect(MainWindow.close)

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giao diện "))
        self.P1.setText(_translate("MainWindow", "1.Lãi đơn"))
        self.P2.setText(_translate("MainWindow", "2.Lãi kép"))
        self.P3.setText(_translate("MainWindow", "3.Tiền gửi hàng tháng"))
        self.P4.setText(_translate("MainWindow", "4.Gửi ngân hàng và rút tiền gửi hàng tháng"))
        self.P5.setText(_translate("MainWindow", "5.Vay vốn trả góp"))
        self.P6.setText(_translate("MainWindow", "6.Lãi kép liên tục"))
        self.label.setText(_translate("MainWindow", " Phần mềm thuộc Ngân Hàng Lạm Phát"))
        self.label1.setText(_translate("MainWindow", " Đây là 7 hình thức dịch vụ tính toán lãi suất\n                  cho quý khách lựa chọn"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
