import mysql.connector
class conexaoBD():
    def __init__(self, host = "localhost", password ="123456", user="root", database="funcionario" ):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        
    def conexao(self):
        self.con = mysql.connector.connect(host = self.host, password = self.password, user= self.user, database= self.database)
        self.cursor = self.con.cursor()
    def desconectar(self):
        self.con.close()
        self.cursor.close()
    def inserir_funcionario(self, nome, sexo):
        self.conect = self.conexao()
        self.sql = f"insert into funcionario (nome,sexo) values('{nome}','{sexo}')"
        self.cursor.execute(self.sql)
        self.con.commit()
        self.disconect = self.desconectar()
    def deletar_usuario(self, id):
        self.conect = self.conexao()
        self.sql = f"delete from funcionario where id = '{id}'"
        self.cursor.execute(self.sql)
        self.con.commit()
        self.disconect = self.desconectar()

class Funcionario(conexaoBD):
    def __init__(self, host="localhost", password="123456", user="root", database="gerenciamento"):
        super().__init__(host, password, user, database)
    def inserir_funcionario(self, nome , sexo):
        self.conect = self.conexao()
        self.sql = f"insert into funcionario (nome,sexo) values('{nome}','{sexo}')"
        self.cursor.execute(self.sql)
        self.con.commit()
        self.disconect = self.desconectar()
    def deletar_usuario(self, id):
        self.conect = self.conexao()
        self.sql = f"delete from funcionario where id = '{id}'"
        self.cursor.execute(self.sql)
        self.con.commit()
        self.disconect = self.desconectar()
    
F1 = Funcionario()
F1.inserir_funcionario()


