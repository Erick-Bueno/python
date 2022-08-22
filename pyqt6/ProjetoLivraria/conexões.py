from socketserver import DatagramRequestHandler
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
       self.sql2 = "Select ano from livros"
       self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
       self.cursor = self.con.cursor()
       self.cursor.execute(self.sql2)
       self.datas = self.cursor.fetchall()
       self.cursor.close()
       self.con.close()
       for c in range(len(self.datas)):
        self.dataa = self.data_atual > self.datas[c][0]
        if self.dataa == True:
            self.sql3 = f"Update livros set Alocado = 'NÃO ALOCADO' where ano = '{self.datas[c][0]}'"
            self.con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "biblioteca")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.sql3)
            self.con.commit()
            self.cursor.close()
            self.cursor.close()
            print(f"{self.datas[c][0]} esta atrasado")
        else: 
            print("não ta atrasado")
            
              
                
        