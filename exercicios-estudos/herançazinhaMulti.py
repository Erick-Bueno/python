class maee:
    def __init__(self, nomee, sexo):
        self.sexo = sexo
        self.nomee = nomee
class paii:
    def __init__(self, nome):
        self.nome = nome
class filho(maee, paii):
    def __init__(self,nome, idade):
        self.idade = idade
        self.nome = nome
        maee.__init__(self, "sirlei", "F")
        paii.__init__(self, "joseleno")
        print("o nome da minha mãe é",self.nomee,"e do meu pai é",self.nome,"e eu tenho ", self.idade, " anos")


filho("erick", 18)




