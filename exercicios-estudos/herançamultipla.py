class nome:
    def falarnome(self, nome):
        self.nome = nome
class idade:
    def falaridade(self,idade):
        self.idade = idade

class mostrar_nome_idade(nome,idade):
    def falartudo(self):
        print("o meu nome é", self.nome, "e a minha idade é", self.idade)
    
    
p1 = mostrar_nome_idade()      
p1.falarnome("erick")
p1.falaridade(16)
p1.falartudo()

