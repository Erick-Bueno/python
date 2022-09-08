class Animal:
    def __init__(self,idade,nome,especie):
        self.idade = idade
        self.nome = nome
        self.especie = especie

class cachorro(Animal):
    def __init__(self, idade, nome, especie, cor):
        self.cor = cor
        super().__init__(idade, nome, especie)



animal1 = cachorro(4,"nina","cachorro","preto")
print(animal1.cor)
