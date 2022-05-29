class Animal:
    def __init__(self, nome, cor, tamanho, correndo = False):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.correndo = correndo

    def correr(self):
        if self.correndo == True:
            print(self.nome,"esta correndo")
            return
        print(self.nome,"não esta correndo")
        self.correndo = True



class Cachorro(Animal):
    def __init__(self):
        super().__init__("cachorro","preto", "grande")

    def correr(self):
        if self.correndo == True:
            print(self.nome,"esta correndo")
            return
        print(self.nome,"não esta correndo")
        self.correndo = True
        





c1 = Cachorro()
c2 = Animal("gato","branca","pequeno")
print(c1.tamanho)
c1.correr()
c2.correr()
    

