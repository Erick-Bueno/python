from tkinter import E
import mysql.connector
host = "localhost"
user = "root"
senha = "123456"
database = "testandu"

conexao = mysql.connector.connect(host = host, user = user, database = database, password = senha)
sql = "Select * from Pessoa"
cursor = conexao.cursor()
cursor.execute(sql)
dados = cursor.fetchall()
conexao.close()
cursor.close()
for c in dados:
    print(c)



def adicionar_user(comando):
    conexao = mysql.connector.connect(host=host, user = user, database = database, password = senha)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    cursor.close
    conexao.close

