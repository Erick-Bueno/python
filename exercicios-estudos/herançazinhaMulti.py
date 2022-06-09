class paii:
    def __init__(self, nome):
        self.nome = nome
class maee:
    def __init__(self, nomee):
        self.nomee = nomee
class filho(paii, maee):
    def __init__(self):
        paii.__init__(self, "SIRLEI")
        maee.__init__(self,"joseleno")
        print("o nome da minha mãe é",self.nomee,"e do meu pai é",self.nome)


filho()


class pai:
    def nome_pai(self,nome):
        self.nome = "Joseleno"
    

class mae:
    def nome_mae(self,nomee):
        self.nomee = "Sirlei"
    

class filhoo(pai, mae):
    def nomespais(self):
        print("o nome da minha mãe é",self.nomee,"e do meu pai é",self.nome)
    
f1 = filhoo()
f1.nome_pai("joseleno")
f1.nome_mae("sirlei")
f1.nomespais()

