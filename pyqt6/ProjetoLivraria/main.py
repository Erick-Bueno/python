from datetime import date
from imgs import icones
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
import mysql.connector
from conexões import Conexao
from enviaremail import enviar_email
import re
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





class App(Conexao):
    #carregando tela e passando as funcoes de evento
    def __init__(self):
        #funcão que e ativada sempre q o sistema inicia
        self.app = QtWidgets.QApplication([])
        self.livraria = uic.loadUi("app.ui")
        self.email = uic.loadUi("email.ui")
        self.livraria.setWindowTitle("livraria")
        self.livraria.pushButton.clicked.connect(self.tela_clietes)
        self.livraria.pushButton_2.clicked.connect(self.tela_livros)
        self.livraria.pushButton_3.clicked.connect(self.tela_alocacao)
        self.livraria.pushButton_9.clicked.connect(self.tela_devolucao)
        self.livraria.pushButton_4.clicked.connect(self.fechar_sistema)
        self.livraria.pushButton_6.clicked.connect(self.adicionar_Livro)
        self.livraria.pushButton_7.clicked.connect(self.verificar_estoque)
        self.livraria.pushButton_8.clicked.connect(self.alocar)
        #setando data atual no dateedit
        data_atual = date.today()
        Data_atual = QDate(data_atual)
        self.livraria.dateEdit.setDate(Data_atual)
        self.livraria.dateEdit_2.setDate(Data_atual)
        self.livraria.pushButton_5.clicked.connect(self.adicionar_cliente)
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
        self.sql8 = "select Nome, Cpf from clientes order by Nome"
        self.con = mysql.connector.connect(host="localhost", user = "root", password = "sirlei231", database = "biblioteca")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.sql8)
        self.nomes = self.cursor.fetchall()
        self.con.close()
        self.cursor.close()
       
        self.livraria.tableWidget.setRowCount(len(self.nomes))
        self.livraria.tableWidget.setColumnCount(2)
        for c in range (len(self.nomes)):
            for i in range(0,2):
                self.livraria.tableWidget.setItem(c,i,QtWidgets.QTableWidgetItem(str(self.nomes[c][i])))

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
        try:
            self.nome_livro = self.livraria.lineEdit_8.text()
            self.nome_livro_validado = self.nome_livro.upper().replace(" ", "")
            self.codigo_livro = self.livraria.lineEdit_11.text()
            self.editora_livro = self.livraria.lineEdit_9.text()
            self.ano_livro = self.livraria.dateEdit.date().toPyDate()
            #validações/tratamento]
            if self.nome_livro == "" or self.codigo_livro == "" or self.editora_livro == "":
                return QMessageBox.warning(self.livraria, "Erro", "preencha todos os campos")
            #dps de tudo validado é chamado o metodo inserir_livro_no_db da classe conexões
            self.inserir_livro_no_db(self.nome_livro_validado,self.codigo_livro, self.editora_livro, self.ano_livro)
            QMessageBox.about(self.livraria,"aviso", "livro adicionado com sucesso")
        except mysql.connector.errors.ProgrammingError:
            QMessageBox.warning(self.livraria,"erro", "codigo invalido, por favor insire apenas os numeros")
    def adicionar_cliente(self):
        self.nome_cliente = self.livraria.lineEdit.text() 
        self.telefone = self.livraria.lineEdit_3.text()
        self.cpf = self.livraria.lineEdit_2.text()
        self.email = self.livraria.lineEdit_4.text()
        self.bairro = self.livraria.lineEdit_7.text()
        self.numero = self.livraria.lineEdit_5.text()
        self.rua = self.livraria.lineEdit_6.text()
        if self.nome_cliente == ""   or self.telefone == "" or self.cpf == "" or self.email == "" or self.bairro == ""  or self.numero == "" or self.rua == "":
            return QMessageBox.warning(self.livraria, "erro", "preencha todos os campos")
        self.cpf_validator = re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', self.cpf)
        if self.cpf_validator == []:
         return QMessageBox.warning(self.livraria,"erro", "insira um cpf valido seguindo o padrão xxx.xxx.xxx-xx" )
        self.nome_cliente_validador = re.findall(r'^[a-zA-Z]{1,}',self.nome_cliente)
        if self.nome_cliente_validador == []:
            return QMessageBox.warning(self.livraria,"erro","insira um nome valido")
        self.sql6 = f"select * from clientes where Nome = '{self.nome_cliente}'"
        self.con = mysql.connector.connect(user = "root", password = "sirlei231",host="localhost", database="biblioteca")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.sql6)
        self.dados = self.cursor.fetchall()
        self.con.close()
        self.cursor.close()
        if len(self.dados) > 0:
            return QMessageBox.warning(self.livraria,"aviso", "nome ja cadastrado")
        self.inserir_cliente(self.nome_cliente, self.cpf_validator[0], self.telefone, self.email, self.numero, self.rua, self.bairro)
        return QMessageBox.about(self.livraria,"aviso","cadastro realizado com sucesso")
    def verificar_estoque(self):
        self.nome_livro_alocado = self.livraria.lineEdit_10.text()
        self.nome_livro_alocado_validado = self.nome_livro_alocado.upper().replace(" ", "")
        if self.nome_livro_alocado == "":
            return QMessageBox.about(self.livraria,"aviso", "informe um livro")
        self.sql10 = f"select count(Nome) from livros where Nome = '{self.nome_livro_alocado_validado}' and Alocado = 'NÃO ALOCADO'"
        self.con = mysql.connector.connect(host = "localhost", password = "sirlei231", user = "root", database = "biblioteca")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.sql10)
        self.dados = self.cursor.fetchall()
        self.con.close()
        self.cursor.close()
        QMessageBox.about(self.livraria, "aviso", f"estoque atual de {self.dados[0][0]}")
    def alocar(self):
        self.codigo_livro_alocado = self.livraria.lineEdit_12.text()
        if self.codigo_livro_alocado == "":
                 return QMessageBox.warning(self.livraria, "erro", "insira o codigo do livro a ser alocado")
        try:
            self.cliente_nome = self.livraria.tableWidget.currentItem().text()
            self.data_alocacao = self.livraria.dateEdit_2.date().toPyDate()
            #pegar id do livro pelo codigo
            self.sql11 = f"select id from livros where codigo = {self.codigo_livro_alocado}"
            self.con = mysql.connector.connect(user = "root", password= "sirlei231", database = "biblioteca", host = "localhost")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql11)
            self.id_livro = self.cursor.fetchall()
            self.con.close()
            self.cursor.close()
            #atualizar livro para alocado
            self.sql12 = f"update livros set Alocado = 'ALOCADO' where codigo = {self.codigo_livro_alocado}"
            self.con = mysql.connector.connect(host = "localhost", password = "sirlei231", database = "biblioteca", user="root")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql12)
            self.con.commit()
            self.con.close()
            self.cursor.close()
            #caso a alocação for feita a partir da seleção do nome
            self.verificar_dado_selecionado =  re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', self.cliente_nome)
            if self.verificar_dado_selecionado == []:
                return QMessageBox.warning(self.livraria, "aviso","selecione o cpf do cliente especifico para efetuar alocação")
            print(self.verificar_dado_selecionado[0])
            
        
               
        except AttributeError:
            return QMessageBox.warning(self.livraria, "erro", "selecione um cliente na lista antes de alocar")
    def enviarr_email(self):
        self.email.show()
        codigo = random.randint(100,999)

        comprador = "mowengine1228@gmail.com"

        host = "smtp.gmail.com"
        port = "587"
        usuario = "erickjb93@gmail.com"
        senha = "zrzhokxrkyzslcgd"

        servidor = smtplib.SMTP(host, port)

        servidor.ehlo()
        servidor.starttls()

        servidor.login(usuario, senha)

        corpo = f"seu codigo é {codigo}"
        msg_email = MIMEMultipart() #um email é codificado em mimemultipart
        msg_email["From"] = usuario
        msg_email["To"] = comprador
        msg_email["Subject"] = "Codigo de confirmação"
        msg_email.attach(MIMEText(corpo, 'plain'))#o conteudo do email é um texto normal 
        servidor.sendmail(msg_email["From"],msg_email["To"],msg_email.as_string())
        print("email enviado")
        servidor.quit()

        

        

    
        
        
        
    



       
   
        

App()

