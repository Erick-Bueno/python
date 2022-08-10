from PyQt5 import QtWidgets
from PyQt5 import uic


app = QtWidgets.QApplication([])
testeee = uic.loadUi("testeee.ui")


testeee.show()
app.exec()
