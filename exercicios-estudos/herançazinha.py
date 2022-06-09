#herança simples adicionando novo atributo na classe filha
class animal:
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor

class gato(animal):
    def __init__(self,nome,cor, raça):
        self.raça = raça
        super().__init__(nome, cor)
    def miar(self):
        print(self.nome,"esta miando e ele tem a raça", self.raça)
------------------------------------------------------------------------------
#herança simples 
class animal:
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor

class gato(animal):
    def miar(self):
        print(self.nome,"esta miando")
g = gato("gersu","preto", "siamez")
g.miar()
