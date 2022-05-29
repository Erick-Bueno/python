import mysql.connector
from enum import Enum

class cargo(Enum):
    V = 1
    F = 2

vigilante = cargo.V.name



class Funcionario:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
    def adicionar_funcs(self,funcionario):
        conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = '123456', database = 'gestao')
        cursor = conexao.cursor()
    
        comando = f'INSERT INTO funcionario (nome, cpf, cargo) VALUES ("{func1.nome}","{func1.cpf}","{vigilante}")'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
while True:
    nome = str(input("informe o seu nome:"))
    cpf = str(input("informe o seu cpf:"))
    func1 = Funcionario(nome,cpf)
    func1.adicionar_funcs(func1)
    continuar = str(input("quer continuar o cadastro?:")).upper()
    if continuar not in 'SN':
        print("digite uma resposta valida")
        continuar = str(input("quer continuar o cadastroo?:")).upper()
    if continuar == "N":
        break


        

