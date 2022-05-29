class Animal:
    def __init__(self,idade,nome,especie):
        self.idade = idade
        self.nome = nome
        self.especie = especie

class cachorro(Animal):
    def comunica(self):
        print(self.nome,"late")



animal1 = cachorro(4,"nina","cachorro")
animal1.comunica()
