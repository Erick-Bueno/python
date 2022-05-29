class Ficha:
    def __init__(self, nome, idade, sexo, xp = False, animal = False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.xp = xp
        self.animal = animal
        print(self.nome,"é o seu nome")
        print(self.idade, "é a sua idade")
        print(self.sexo, "é o seu sexo")
    def experiencia(self, experience):
        print(self.nome,"tem experiencia",experience)
        self.xp = True
    def gato(self, cat):
        print(self.nome,"tem um gato chamado",cat)
        self.animal = True

p1 = Ficha("erick",18,"masculino")
p1.experiencia("sim")
p1.gato("gerson")


