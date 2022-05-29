from cProfile import label
from cgitb import text
from dataclasses import dataclass
from distutils.filelist import findall
from email import message
from errno import ENETUNREACH
from inspect import Attribute
from tkinter import *
import tkinter
from tkinter import messagebox
from turtle import back, color, onclick
from unicodedata import digit
from winreg import EnableReflectionKey
import mysql
import mysql.connector
from setuptools import Command
import conexão
from pip import main
import re
from http import server
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





try:
    class aplicaçao():
        def __init__(self, janela = Tk()):
            self.janela = janela
            self.config()
            self.frames()
            self.widgets()
            self.janela.mainloop()
        def inserir(self):
            self.vnome = self.input_label1.get()
            self.vsexoo = self.vsexo.get()
            self.vcodigo = self.input_label3.get()
            self.vcpf = self.label4_input.get()
            self.vsenha = self.input_label5.get()
            self.vgmail = self.input_label7.get()
            self.especiais = ".-"
            for c in self.especiais:
                self.vcpf = self.vcpf.replace(c,"")
            if self.vcpf != "" and self.vnome != "" and self.vsexoo != "" and self.vcodigo  != "" and self.vcpf  != "" and self.vsenha  != "" and self.vgmail != "" :
                    self.validador = (re.findall(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',self.vcpf))
                    if self.validador == []:
                        messagebox.showinfo(title="aviso",message="cpf invalido")
                    else:    
                        try:
                            self.sql = f"Select nome from Pessoas where nome = '{self.vnome}'"
                            con =  mysql.connector.connect(host="localhost", password ="123456",database="banco", user = "root")
                            cursor = con.cursor()
                            cursor.execute(self.sql)
                            dado = cursor.fetchall()
                            cursor.close()
                            con.close()
                            if self.vnome.isdigit():
                                    messagebox.showinfo(title="aviso",message="nome invalido")
                                
                            else:   
                                    if len(dado) != 0:
                                        messagebox.showinfo(title="aviso",message="nome ja cadastrado")
                                    else:
                                        self.validar_senha = (re.findall(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\u0020-\u002f-\u003A-\u0040\-\u005B-\u0060-\u007B-\u007E]).{8}',self.vsenha))
                                        if self.validar_senha == []:
                                            messagebox.showinfo(title="aviso",message="senha invalida, verifique se a sua senha atende aos requisitos: ter pelo menos 8 caracteres, contendo numero letra maiscula e caracter especial")
                                        else:
                                            if "gmail" not in self.vgmail:
                                                messagebox.showinfo(title="aviso",message="Informe um gmail valido, lembre-se de conferir se o G de gmail esta minusculo")
                                            else:

                                                self.sql = f"Insert Into Pessoas (id, nome, sexo, cpf, senha, gmail) Values ('{self.vcodigo}','{self.vnome}','{self.vsexoo}','{self.vcpf}','{self.vsenha}', '{self.vgmail}')" 
                                                conexão.conexaoDb(self.sql)
                                                print("gravado")
                                                print(self.vcodigo)
                                                messagebox.showinfo(title="aviso",message=f"{self.vnome} seu registro foi realizado com sucesso!!!")
                                                self.abrir_janela()
                        except AttributeError:
                            messagebox.showinfo(title="aviso",message="preencha todos os campos")
                        except mysql.connector.IntegrityError:
                            messagebox.showinfo(title="aviso",message="o codigo informado ja foi cadastrado")
                        
                        

            else:
                messagebox.showinfo(title="aviso",message="preencha tudo antes de inserir")
        def inserir_item(self):
            self.codigo_usuario = self.input_label3.get()
            conexão.conexaoDb(self.sql)
            print(self.codigo_usuario)
        def deletar(self):
            self.sql = "Delete from funcionario where id = 4"
            conexão.conexaoDb(self.sql)
            print("deletado")
        def config(self):
            self.janela.title("gerenciamento")
            self.janela.configure(background="#473727")     
            self.janela.geometry("600x200")
            self.janela.resizable(True, True)
            self.janela.maxsize(width="1920", height="1080" )
            self.janela.minsize(width="640", height="480")
        def limpar(self):
            self.input_label1.delete(0, END)
            self.input_label3.delete(0, END)
            self.label4_input.delete(0, END)
            self.input_label5.delete(0, END)
        
        def sair(self):
            self.nova_janela.destroy()
        def mostrar_janela(self):
            self.janela.deiconify()
            self.nova_janela.withdraw()
        def fechar_janela__anterior(self):
            self.janela.destroy() #fecha a janela anterior
        def fechar_janela_anterior2(self):
            self.tela_logar.destroy()
        def abrir_janela(self):
            self.janela.destroy()
            self.nova_janela = Tk()
            self.nova_janela.title("Cadastrar item")
            self.nova_janela.configure(background="#473727")
            self.nova_janela.geometry("600x200") 
            self.nova_janela.resizable(True, True)
            self.nova_janela.maxsize(width="1920", height="1080")
            self.nova_janela.minsize(width="640", height="480")
            self.frame3 = Frame(self.nova_janela, bd=4, highlightbackground="gray", highlightthickness=2)
            self.frame3.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.4)
            self.frame4 = Frame(self.nova_janela, bd=4,  highlightbackground="gray",highlightthickness=2)
            self.frame4.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.47)
            self.button3 = Button(self.frame3, text="Sair", command = self.sair)
            self.button3.place(relx=0.9, rely=0.8, relheight=0.2, relwidth=0.08)
            self.label_nome_produto=Label(self.nova_janela, text="Nome Do Produto")
            self.label_nome_produto.place(relx= 0.05, rely=0.08, relheight=0.08, relwidth=0.2)
            self.input_nome_produto = Entry(self.nova_janela)
            self.input_nome_produto.place(relx=0.07, rely=0.15, relheight=0.04, relwidth=0.55)
            self.button4 = Button(self.frame3, text="confirmar", command=self.confirmar)
            self.button4.place(relx=0.77, rely=0.8, relheight=0.2, relwidth=0.1)
            self.label_preço_produto = Label(self.nova_janela, text="Preço")
            self.label_preço_produto.place(relx= 0.05, rely=0.2, relheight=0.08,relwidth=0.09)
            self.input_preço_produto = Entry(self.nova_janela)
            self.input_preço_produto.place(relx=0.07, rely=0.27, relheight=0.04, relwidth=0.2)
            self.label_quant = Label(self.nova_janela, text="Quantidade")
            self.label_quant.place(relx=0.4, rely=0.2, relheight=0.08, relwidth=0.1 )
            self.input_quant = Entry(self.nova_janela)
            self.input_quant.place(relx=0.4, rely=0.27, relheight=0.04, relwidth=0.2)

            self.nova_janela.mainloop()
        def confirmar(self):
            self.vnome_produto = self.input_nome_produto.get()
            self.vquantidade = self.input_quant.get()
            self.vpreço = self.input_preço_produto.get()
            if self.vnome_produto == "" and self.vquantidade == "" and self.vpreço == "":
                messagebox.showinfo(title="aviso", message = "Preencha tudo antes de inserir o produto")
            else:
                 self.nome = (re.findall(r'^[a-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑA-Z\s]{1,}$', self.vnome_produto))
                 if self.nome == []:
                    messagebox.showinfo(title="aviso", message="Nome invalido para produto")

                 else:
                    self.quantia = (re.findall(r'\d{1,}',self.vquantidade))
                    if self.quantia == []:
                         messagebox.showinfo(title="aviso", message="valor invalido para quantidade")
                    else:
                        if "," in self.vquantidade:
                            messagebox.showinfo(title="aviso", message="valor invalido para quantidade")
                        else:
                            if " " in self.vquantidade:
                                messagebox.showinfo(title="aviso", message="Não de espaços ao colocar o valor para quantidade")
                                
                            else:
                                self.preçu = (re.findall(r'\d{1,}',self.vpreço)) 
                                if self.preçu == []:
                                    messagebox.showinfo(title="aviso", message="valor invalido para preço")
                                else:
                                    if "," in self.vpreço:
                                        self.vpreço = self.vpreço.replace(",",".")
                                        messagebox.showinfo(title="aviso", message="valor invalido para preço")
                                    else:
                                        if " " in self.vpreço:
                                            messagebox.showinfo(title="aviso", message="Não de espaços ao colocar o valor para preço")
                                        else:
                                            self.sql = f"Insert into Produto (nome, preço, quantidade) Values ('{self.vnome_produto}', {self.vpreço}, {self.vquantidade})"
                                            conexão.conexaoDb(self.sql)
                                            self.sql2 = f"Select id_produto from Produto where nome = '{self.vnome_produto}'"
                                            con = mysql.connector.connect(host="localhost", password ="123456",database="banco", user = "root")
                                            cursor = con.cursor()
                                            cursor.execute(self.sql2)
                                            id_produto = cursor.fetchall()
                                            cursor.close()
                                            con.close()
                                            self.sql = f"Insert into compra (id_pessoa, produto_id) Values('{self.vcodigo[0][0]}','{id_produto[0][0]}')"
                                            conexão.conexaoDb(self.sql)
                                            messagebox.showinfo(title="aviso", message="cadastro de produto realizado com sucesso")

        def logarr(self):
            
            try:
                
                self.nome_logar = self.input_nome.get()
                self.senha_logar = self.input_senha.get()
        
                self.sql = f"Select senha from Pessoas where nome = '{self.nome_logar}'"
                con =  mysql.connector.connect(host="localhost", password ="123456",database="banco", user = "root")
                cursor = con.cursor()
                cursor.execute(self.sql)
                dado = cursor.fetchall()
                cursor.close()
                con.close()
                
                if dado[0][0] == self.senha_logar:
                    self.sql = f"Select id from Pessoas where nome = '{self.nome_logar}'"
                    con =  mysql.connector.connect(host="localhost", password ="123456",database="banco", user = "root")
                    cursor = con.cursor()
                    cursor.execute(self.sql)
                    id = cursor.fetchall()
                    cursor.close()
                    con.close()
                    self.vcodigo = id
                    print(self.vcodigo[0][0])
                    messagebox.showinfo(message="logado com sucesso")
                    self.abrir_janela()
                else:
                    messagebox.showinfo(message="senha incorreta")
            except:
                messagebox.showinfo(message="informe valores validos")
        def tela_login(self):
            self.janela.withdraw()
            self.tela_logar = Toplevel()
            self.tela_logar.title("login")
            self.tela_logar.geometry("600x200")
            self.tela_logar.resizable(True, True)
            self.tela_logar.maxsize(width="1920", height="1080")
            self.tela_logar.minsize(width="640", height="480")
            self.logar_nome = Label(self.tela_logar, text="Login(nome)",font=("Times New Roman", 12, "bold" ))
            self.logar_nome.place(relx= 0.7, rely=0.3, relheight=0.1, relwidth=0.25)
            self.input_nome = Entry(self.tela_logar)
            self.input_nome.place(relx= 0.7, rely=0.38, relheight=0.03, relwidth=0.25)

            self.logar_senha = Label(self.tela_logar, text="Senha",font=("Times New Roman", 12, "bold"))
            self.logar_senha.place(relx=0.77, rely=0.44,relheight=0.03, relwidth=0.08)
            self.input_senha = Entry(self.tela_logar, show="*")
            self.input_senha.place(relx=0.7, rely=0.49, relheight=0.03, relwidth=0.25)

            self.label_conta = Label(self.tela_logar, text="JA TEM UMA CONTA?", font=("Arial", 12, "bold"))
            self.label_conta.place(relx=0.67, rely=0.25, relheight=0.06, relwidth=0.3)
            self.botao_conta = Button(self.tela_logar, text="Logar",font=("Times New Roman", 12), command=self.logarr)
            self.botao_conta.place(relx=0.7, rely=0.8, relheight=0.08, relwidth=0.08)
            
            

        def frames(self):
            self.frame1 = Frame(self.janela, bd=4, highlightbackground="gray", highlightthickness=2)
            self.frame1.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)
        def widgets(self):
            self.botao_inserir = Button(self.janela, text="Inserir", command=self.inserir, font=("Times New Roman", 12))
            self.botao_inserir.place(relx=0.50, rely=0.8, relwidth=0.08, relheight=0.08)
            self.botao_limpar = Button(self.janela, text="limpar", command=self.limpar, font=("Times New Roman", 12))
            self.botao_limpar.place(relx=0.39, rely=0.8, relwidth=0.08, relheight=0.08)
            
            self.label1 = Label(self.janela, text="Nome",font=("Times New Roman", 12, ))
            self.label1.place(relx= 0.2, rely=0.20, relheight=0.1, relwidth=0.08)
            self.input_label1 = Entry(self.janela)
            self.input_label1.place(relx=0.2, rely=0.30, relheight=0.04, relwidth=0.6)


            self.label3 = Label(self.janela, text="Código",font=("Times New Roman", 12))
            self.label3.place(relx= 0.065, rely=0.70, relheight=0.1, relwidth=0.08)
            self.input_label3 = Entry(self.janela)
            self.input_label3.place(relx=0.077, rely=0.8, relheight=0.06, relwidth=0.06)
            
            self.label4 = Label(self.janela, text="Cpf",font=("Arial", 12))
            self.label4.place(relx= 0.2, rely=0.36, relheight=0.1, relwidth=0.08)
            self.label4_input = Entry(self.janela)
            self.label4_input.place(relx=0.2, rely=0.45, relheight=0.04, relwidth=0.2)


            self.botao_next = Button(self.janela, text="Next", font=("Times New Roman", 12,),command=self.abrir_janela)
            self.botao_next.place(relx=0.8, rely=0.8, relheight=0.08, relwidth=0.08)

            self.label5 = Label(self.janela, text="Senha",font=("Times New Roman", 12))
            self.label5.place(relx=0.5, rely=0.36,relheight=0.1, relwidth=0.08)
            self.input_label5 = Entry(self.janela, show="*")
            self.input_label5.place(relx=0.5, rely=0.45, relheight=0.04, relwidth=0.3)

            self.botao_conta = Button(self.janela, text="Login",font=("Times New Roman", 12), command=self.tela_login)
            self.botao_conta.place(relx=0.7, rely=0.8, relheight=0.08, relwidth=0.08)

            self.label6 = Label(self.janela, text="CADASTRO", font=("Verdana", 25, "bold"))
            self.label6.place(relx=0.25, rely=0.1, relheight=0.06, relwidth=0.5)
            
            self.vsexo = StringVar()
            self.masculino = Radiobutton(self.janela, text="Masculino", value="M",  variable=self.vsexo)
            self.masculino.place(relx=0.46, rely=0.70, relheight=0.06, relwidth=0.2)

            self.feminino = Radiobutton(self.janela, text="Feminino", value="F",  variable=self.vsexo)
            self.feminino.place(relx=0.3, rely=0.70, relheight=0.06, relwidth=0.2)
            
            self.label7= Label(self.janela, text="Gmail",font=("Times New Roman", 12, ))
            self.label7.place(relx= 0.2, rely=0.54, relheight=0.05, relwidth=0.08)
            self.input_label7 = Entry(self.janela)
            self.input_label7.place(relx=0.2, rely=0.60, relheight=0.04, relwidth=0.6)



    
            



except:
    print("valores invalidos")           
        


        
        


aplicaçao()




    


        
 
        
        

