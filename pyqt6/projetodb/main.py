import cProfile
from multiprocessing.reduction import send_handle
from pickle import FALSE
from PyQt5 import uic,QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from pandas import DatetimeTZDtype
import icons
import mysql.connector
import re
import webbrowser

def acessar_email():
    new=2
    url="https://www.gmail.com/"

    webbrowser.open(url,new=new)

def logar():

    projetoo.frame_2.close()
    
    
def voltar_logar():
    projetoo.frame_2.show()
def registrar():
    

    
    global codigo
    global masculino
    global nome
    global cpf
    global email
    nome = projetoo.lineEdit.text()
    senha= projetoo.lineEdit_2.text()
    cpf = projetoo.lineEdit_3.text()
    email = projetoo.lineEdit_4.text()
    codigo = projetoo.lineEdit_5.text()
    masculino = projetoo.radioButton.text()
    feminino = projetoo.radioButton_2.text()
    outtro = projetoo.radioButton_3.text()
    if nome == "" or senha == "" or cpf == "" or email == "" or codigo == "" or projetoo.radioButton.isChecked() == False and   projetoo.radioButton_2.isChecked() == False and  projetoo.radioButton_3.isChecked() == False:
        QMessageBox.warning(projetoo, "Aviso", "PREENCHA TODOS OS CAMPOS")
    else:
        validar_nome = (re.findall(r'^[a-zA-Z]{1,}',nome))
        validar_cpf = (re.findall(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',cpf))
        if validar_cpf == []:
             QMessageBox.warning(projetoo, "Aviso", " CPF INVALIDO")
        else:
            if validar_nome == []:
                QMessageBox.warning(projetoo, "AVISO", "Insira um valor de nome valido")
            else:
                try:
                    sql = f"Select nome from Pessoas where nome = '{nome}'"
                    con = mysql.connector.connect(host = "localhost", user="root", password="123456",database="banco")
                    cursor = con.cursor()
                    cursor.execute(sql)
                    dado_nome = cursor.fetchall()
                    con.close()
                    cursor.close()
                    if len(dado_nome) !=0:
                        QMessageBox.warning(projetoo,"AVISO", "ESSE NOME JA FOI CADASTRO, TENTE OUTRO")
                    else:
                        validador_senha = (re.findall(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\u0020-\u002f-\u003A-\u0040\-\u005B-\u0060-\u007B-\u007E]).{8}',senha))
                        if validador_senha == []:
                            QMessageBox.warning(projetoo,"Aviso","senha invalida, verifique se a sua senha atende aos requisitos: ter 8 caracteres, contendo numero letra maiscula e caracter especial")
                        else:
                            if "gmail" not in email:
                                QMessageBox.warning(projetoo, "AVISO", "INFORME UM GMAIL VALIDO")
                            else:
                                if projetoo.radioButton.isChecked():
                                    sql2 = f"Insert Into Pessoas (id,nome,sexo,cpf,senha,gmail) values ('{codigo}','{nome}','M','{cpf}','{senha}','{email}')"
                                    con2 = mysql.connector.connect(host = "localhost", user="root",password="123456", database="banco")
                                    cursor2 = con2.cursor()
                                    cursor2.execute(sql2)
                                    con2.commit()
                                    con2.close()
                                    cursor2.close()  
                                    QMessageBox.about(projetoo,"AVISO", "REGISTRO REALIZADO COM SUCESSO")
                                    limpar() 
                                if projetoo.radioButton_2.isChecked():
                                    sql2 = f"Insert Into Pessoas (id,nome,sexo,cpf,senha,gmail) values ('{codigo}','{nome}','F','{cpf}','{senha}','{email}')"
                                    con2 = mysql.connector.connect(host = "localhost", user="root",password="123456", database="banco")
                                    cursor2 = con2.cursor()
                                    cursor2.execute(sql2)
                                    con2.commit()
                                    con2.close()
                                    cursor2.close()  
                                    QMessageBox.about(projetoo,"AVISO", "REGISTRO REALIZADO COM SUCESSO") 
                                    limpar()
                                if projetoo.radioButton_3.isChecked():
                                    sql2 = f"Insert Into Pessoas (id,nome,sexo,cpf,senha,gmail) values ('{codigo}','{nome}','O','{cpf}','{senha}','{email}')"
                                    con2 = mysql.connector.connect(host = "localhost", user="root",password="123456", database="banco")     
                                    cursor2 = con2.cursor()
                                    cursor2.execute(sql2)
                                    con2.commit()
                                    con2.close()
                                    cursor2.close()
                                    QMessageBox.about(projetoo,"AVISO", "REGISTRO REALIZADO COM SUCESSO")
                                    limpar()
            
                                
                except mysql.connector.errors.IntegrityError:
                    QMessageBox.warning(projetoo,"AVISO","o codigo informado ja foi cadastrado ")
                except mysql.connector.errors.DatabaseError:
                    QMessageBox.warning(projetoo,"AVISO","codigo invalido")
def Login():
    nome_login = projetoo.lineEdit_6.text()
    senha_login = projetoo.lineEdit_7.text()
    sql = f"Select nome From Pessoas where nome =  '{nome_login}'"
    con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database = "banco")
    cursor = con.cursor()
    cursor.execute(sql)
    dados3 = cursor.fetchall()
    cursor.close()
    con.close()
    if len(dados3) == 0 :
        QMessageBox.warning(projetoo, "Aviso", "Nome n??o cadastrado") 
    else:
        sql = f"Select senha from Pessoas where nome = '{nome_login}'"
        con = mysql.connector.connect(host= "localhost", password = "123456", user = "root", database = "banco")
        cursor = con.cursor()
        cursor.execute(sql)
        dados4 = cursor.fetchall()
        cursor.close()
        con.close()
        if dados4[0][0] != senha_login:
            QMessageBox.warning(projetoo,"Aviso","Senha incorreta" )
        else:
            sql = f"Select id from Pessoas where nome = '{nome_login}'"
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database= "banco")
            cursor = con.cursor()
            cursor.execute(sql)
            codigo = cursor.fetchall()
            cursor.close()
            con.close()
            QMessageBox.about(projetoo,"Aviso","Logado Com Sucesso")
            print(codigo[0][0])
            projetoo.close()
            produto.show()


def esqueceu_senha():
    

def limpar():
    projetoo.lineEdit.clear()     
    projetoo.lineEdit_2.clear()
    projetoo.lineEdit_3.clear()
    projetoo.lineEdit_4.clear()
    projetoo.lineEdit_5.clear()

  
    

app = QtWidgets.QApplication([])
projetoo = uic.loadUi("projetoo.ui")
produto = uic.loadUi("tela_produto.ui")
projetoo.setWindowTitle("Cadastro")
projetoo.setWindowIcon(QtGui.QIcon("logo.png"))
projetoo.pushButton.clicked.connect(registrar)
projetoo.pushButton_2.clicked.connect(logar)
projetoo.pushButton_5.clicked.connect(voltar_logar)
projetoo.pushButton_3.clicked.connect(Login)
projetoo.pushButton_6.clicked.connect(acessar_email)


projetoo.show()
app.exec()