from imgs import icones
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
import mysql.connector
from conexões import Conexao

class App(Conexao):
    #carregando tela e passando as funcoes de evento
    def __init__(self):
        self.verificando()
        self.app = QtWidgets.QApplication([])
        self.livraria = uic.loadUi("app.ui")
        self.livraria.setWindowTitle("livraria")
        self.livraria.pushButton.clicked.connect(self.tela_clietes)
        self.livraria.pushButton_2.clicked.connect(self.tela_livros)
        self.livraria.pushButton_3.clicked.connect(self.tela_alocacao)
        self.livraria.pushButton_9.clicked.connect(self.tela_devolucao)
        self.livraria.pushButton_4.clicked.connect(self.fechar_sistema)
        self.livraria.pushButton_6.clicked.connect(self.adicionar_Livro)
        self.livraria.show()
        self.app.exec()
    #metodo q direiciona para tela de cadastro de clientes
    def tela_clietes(self):
        self.livraria.frame.show()
        self.livraria.frame_3.hide()
        self.livraria.frame_4.hide()
        self.livraria.frame_5.hide()
    #metodo q direciona para tela de cadastro de livros
    def tela_livros(self):

        self.livraria.frame_3.show()
        self.livraria.frame_4.show()
        self.livraria.frame_5.show()
    #metodo q direciona para tela de alocação
    def tela_alocacao(self):
        self.livraria.frame_3.hide()
        self.livraria.frame_4.show()
        self.livraria.frame_5.hide()
    #metodo q direciona para tela de devolução
    def tela_devolucao(self):
        self.livraria.frame_3.hide()
        self.livraria.frame_4.show()
        self.livraria.frame_5.show()
    #metodo q fecha o sistema
    def fechar_sistema(self):
        self.livraria.close()
    #metodo q adiciona um novo registro de livro no database
    def adicionar_Livro(self):
        self.nome_livro = self.livraria.lineEdit_8.text()
        self.codigo_livro = self.livraria.lineEdit_11.text()
        self.editora_livro = self.livraria.lineEdit_9.text()
        self.ano_livro = self.livraria.dateEdit.date().toPyDate()
        #validações/tratamentos


        #dps de tudo validado é chamado o metodo inserir_livro_no_db da classe conexões
        self.inserir_livro_no_db(self.nome_livro,self.codigo_livro, self.editora_livro, self.ano_livro)
        QMessageBox.about(self.livraria,"aviso", "livro adicionado com sucesso")

    

    



       
   
        

App()