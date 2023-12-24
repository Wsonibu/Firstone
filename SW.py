import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"
class Ui_SW(object):
    def openwindow(self):
        from home import MyObject
        self.window = QtWidgets.QMainWindow()
        self.ui=MyObject()
        self.ui.setupUi(self.window)
        self.window.show()
    def backwindow(self):
        from Window import Ui_home
        self.window1= QtWidgets.QMainWindow()
        self.ui=Ui_home()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 10, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 80, 350, 121))
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 79, 200, 101))
        self.groupBox.setObjectName("groupBox")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 60, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 28, 150, 120))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QPushButton(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 150, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QPushButton(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 123, 80, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QPushButton(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 123, 80, 21))
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QPushButton(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 150, 80, 21))
        self.label_13.setObjectName("TinhLai")
        self.label_17 = QtWidgets.QCheckBox(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(140, 2, 86, 17))
        self.label_17.setObjectName("c")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(40, 210, 50, 21))
        self.Back.setObjectName("label_9")

        self.Back.clicked.connect(self.backwindow)
        self.Back.clicked.connect(MainWindow.close)
        self.label_8.clicked.connect(self.openwindow)


        self.sex = QtWidgets.QComboBox(self.groupBox)
        self.sex.setGeometry(QtCore.QRect(80, 70, 69, 22))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.fullname = QtWidgets.QLineEdit(self.groupBox)
        self.fullname.setGeometry(QtCore.QRect(80, 40, 191, 20))
        self.fullname.setObjectName("fullname")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 10, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ứng dụng tính toán lãi suất"))
        self.label.setText(_translate("MainWindow", "Dịch vụ ngân hàng"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin khách hàng"))
        self.label_5.setText(_translate("MainWindow", "Giới tính"))
        self.sex.setItemText(0, _translate("MainWindow", "Nam"))
        self.sex.setItemText(1, _translate("MainWindow", "Nữ"))
        self.label_4.setText(_translate("MainWindow", "Họ và tên"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Yêu cầu"))
        self.label_13.setText(_translate("MainWindow", "Tính Lãi %"))
        self.label_6.setText(_translate("MainWindow", "(kỳ hạn tính theo năm)"))
        self.label_7.setText(_translate("MainWindow", "Tính Gốc"))
        self.label_8.setText(_translate("MainWindow", "Tính Tổng"))
        self.label_9.setText(_translate("MainWindow", "Tính Kỳ hạn"))
        self.Back.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    SW = QtWidgets.QMainWindow()
    ui = Ui_SW()
    ui.setupUi(SW)
    SW.show()
    sys.exit(app.exec_())