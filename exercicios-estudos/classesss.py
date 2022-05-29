class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Gato(Animal):
    def __init__(self, nome, cor, altura):
        self.altura = altura
        super().__init__(nome,cor)
    def Miar(self):
        print(self.nome,"tem o tamanho",self.altura, "a cor",self.cor, "e esta miando")


G1 = Gato("gerson","cinza","alto")
G1.Miar()





