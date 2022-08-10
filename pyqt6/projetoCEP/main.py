from PyQt5 import QtWidgets
from PyQt5 import uic
import requests



def consultar():
    CEP = cep.lineEdit.text()
    api = requests.get(f"https://cep.awesomeapi.com.br/json/{CEP}")
    dados = api.json()
    endereço = dados['address']
    bairro = dados['district']
    ceep = dados['cep']
    cidade = dados['city']
    UF = dados['state']
    cep.label_8.setText(endereço)
    cep.label_9.setText(bairro)
    cep.label_11.setText(ceep)
    cep.label_10.setText(cidade)
    cep.label_12.setText(UF)




app = QtWidgets.QApplication([])
cep = uic.loadUi("cep.ui")
cep.setWindowTitle("BsCEP")
cep.pushButton.clicked.connect(consultar)

cep.show()
app.exec()