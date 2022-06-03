from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
class aplicaçao:
    def __init__(self, app = QtWidgets.QApplication([]), projetoo = uic.loadUi("projetoo.ui") ):
        self.app = app
        self.projetoo = projetoo
        self.app.exec()
        self.projetoo.show()
        
aplicaçao()