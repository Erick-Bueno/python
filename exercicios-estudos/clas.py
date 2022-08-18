class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    def andar(self):
        print(f"seu carro de cor {self.cor} e marca {self.marca} esta andando" )
class gipe(Carro):
    def __init__(self, marca, cor, rodas):
        self.rodas = rodas
        super().__init__(marca, cor)
        

gipe1 = gipe("GIPÃO","roda", 6)

print(gipe1.rodas)