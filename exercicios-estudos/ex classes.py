class Pessoa:
    def __init__(self,nome, correndo = False, comendo = False):
        self.nome = nome
        self.comendo = comendo
        self.correndo = correndo
    def comer(self):
        if self.comendo == True:
            print("ja esta comendo")
            return
        print("esta comendo")
        self.comendo = True
    def parar_comer(self):
        if self.comendo == False:
            print("não esta comendo")
            return
        print("parou de comer")
        self.comendo = False
p1 = Pessoa("erick")
p1.comer()
p1.parar_comer()
p1.parar_comer()
p1.comer()


