class Pessoa:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome
        print(self.nome,"tem",self.idade,"anos")


class Usuario:
    def __init__(self):
        self.pessoa = Pessoa(16,"erick")

pessoa1 = Pessoa(18,"ana")
pessoa2 = Usuario()
