from socketserver import DatagramRequestHandler
from threading import local
import mysql.connector
from http import server
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

class Conexao:
    def __init__(self):
        pass
    def inserir_livro_no_db(self, livro_nome, livro_codigo, livro_editora, data_livro):
        self.livro_nome = livro_nome
        self.livro_codigo = livro_codigo
        self.livro_editora = livro_editora
        self.data_livro = data_livro
        self.sql = f"Insert into livros (codigo, Nome, Editora, ano) values ({self.livro_codigo}, '{self.livro_nome}', '{self.livro_editora}', '{self.data_livro}')"
        self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.sql)
        self.con.commit()
        self.cursor.close()
        self.con.close()
    def verificando(self):
       self.data_atual = date.today()
       self.sql2 = "select dataa from alocacao inner join clientes on clientes.id = alocacao.id_cliente inner join livros on livros.id = alocacao.id_livro;"
       self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
       self.cursor = self.con.cursor()
       self.cursor.execute(self.sql2)
       self.datas = self.cursor.fetchall()
       self.cursor.close()
       self.con.close()
       for c in range(len(self.datas)):
        self.dataa = self.data_atual > self.datas[c][0]
        if self.dataa == True:
            self.sql3 = f"update alocacao set alocacao.atraso = 'True' where alocacao.dataa = '{self.datas[c][0]}'"
            self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql3)
            self.con.commit()
            self.cursor.close()
            self.cursor.close()
            self.sql4 = f"select clientes.Nome from alocacao inner join clientes on clientes.id = alocacao.id_cliente inner join livros on livros.id = alocacao.id_livro where alocacao.dataa='{self.datas[c][0]}'"
            self.con = mysql.connector.connect(host = "localhost", user = "root", password= "sirlei231", database = "biblioteca")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql4)
            self.user_name = self.cursor.fetchall()
            self.con.close()
            self.cursor.close()
            
            for i in range(len(self.user_name)):
                self.sql5 = f"update clientes set Bloqueado = 'True' where Nome = '{self.user_name[i][0]}'"
                self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
                self.cursor = self.con.cursor()
                self.cursor.execute(self.sql5)
                self.con.commit()
                self.cursor.close()
                self.cursor.close()
        else: 
            print("tudo certo")
    
    def inserir_cliente(self, nome_cliente, cpf_validator, telefone, email, numero, rua,bairro):
        self.nome_cliente = nome_cliente
        self.cpf_validator = cpf_validator
        self.telefone = telefone
        self.email= email
        self.numero = numero
        self.rua = rua
        self.bairro = bairro
        self.sql7 = f"insert into clientes(Nome, Cpf, Telefone, Email, Numero, Rua, Bairro) values ('{self.nome_cliente}', '{self.cpf_validator}', '{self.telefone}','{self.email}','{self.numero}','{self.rua}', '{self.bairro}')"
        self.con = mysql.connector.connect(user = "root", password = "sirlei231", database = "biblioteca", host = "localhost")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.sql7)
        self.con.commit()
        self.con.close()
        self.cursor.close()
    
   

    
            
              
                
        