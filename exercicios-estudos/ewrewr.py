class brinquedo:
    def __init__(self,cor,formato):
        self.cor = cor
        self.formato = formato
        self.brincadeira = None

class criança:
    def __init__(self,nome):
        self.nome = nome
    def brincar(self):
        print(self.nome,"esta brincando")
    


b = brinquedo("verde","quadrado")
c = criança("ana")
brinquedo.brincadeira = criança
brinquedo.brincadeira.brincar()


        