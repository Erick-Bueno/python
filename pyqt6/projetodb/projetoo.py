# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projetoo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 600)
        MainWindow.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(370, 50, 511, 471))
        self.frame.setStyleSheet("background-color:white;\n"
"border-bottom-right-radius:50px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 150, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:solid;\n"
"border-color:black;\n"
"border-bottom-width:2px;\n"
"\n"
"\n"
"")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 150, 41, 41))
        self.label.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:solid;\n"
"border-color:black;\n"
"border-bottom-width:2px;\n"
"padding-left:5px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 211, 31))
        self.label_2.setStyleSheet("color:#E68A8A;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-bottom-width:2px;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 200, 41, 41))
        self.label_3.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-bottom-width:2px;\n"
"padding-left:5px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 250, 221, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-bottom-width:2px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 300, 221, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-bottom-width:2px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 250, 41, 41))
        self.label_4.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-bottom-width:2px;\n"
"padding-left:5px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(120, 300, 41, 41))
        self.label_5.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-bottom-width:2px;\n"
"padding-left:5px;")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 410, 241, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:#E68A8A;\n"
"    font: 8pt \"Verdana\";\n"
"    border-radius:5px;\n"
"    color:white;\n"
"    border-style:outset;\n"
"    border-bottom-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#B36B6B;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(150, 350, 71, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 350, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 350, 51, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 410, 41, 51))
        self.lineEdit_5.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-style:outset;\n"
"border-top-width:1px;\n"
"border-bottom-width:1px;\n"
"\n"
"\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 410, 41, 51))
        self.label_6.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"padding-left:5px;\n"
"border-style:outset;\n"
"border-bottom-width:1px;\n"
"border-top-width:1px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 50, 341, 471))
        self.frame_2.setStyleSheet("background-color: #E68A8A;\n"
"border-top-left-radius:50px;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(60, 170, 231, 31))
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(80, 200, 181, 51))
        self.textEdit.setStyleSheet("color: rgb(221, 221, 221);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 280, 75, 31))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"    font: 8pt \"Verdana\";\n"
"    border-radius:5px;\n"
"    color:white;\n"
"    border-color:#665C5C;\n"
"    border-style:outset;\n"
"    border-width:2px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#665C5C;\n"

"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/pessoa.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">CRIE SUA CONTA</span></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/cadeado.png\"/></p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/carteira-de-motorista.png\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/o-email.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "REGISTRAR"))
        self.radioButton.setText(_translate("MainWindow", "Masculino"))
        self.radioButton_2.setText(_translate("MainWindow", "Feminino"))
        self.radioButton_3.setText(_translate("MainWindow", "Outro"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "C??digo"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/id-do-rosto.png\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">JA TEM UMA CONTA?</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Se ja possui uma conta acesse-a atrav??s do bot??o abaixo</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
