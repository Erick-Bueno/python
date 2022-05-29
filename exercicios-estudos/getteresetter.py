class Pessoa:
    def __init__(self, nome,idade):
        self.idade = idade
        self.nome = nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,valor):
        self.__nome = valor.upper()



p1 = Pessoa("erick",18)
print(p1.nome)
