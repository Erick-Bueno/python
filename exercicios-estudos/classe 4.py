class bola:
    def __init__(self, cor, circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        print(" a circunferencia da bola mede:",self.circunferencia)
        print(" o material da bola é:", self.material)
    def trocaCor(self):
        self.cor = str(input("cor:"))
    def mostraCor(self):
        print("a cor da bola é:",self.cor)





raio = float(input("informe o raio da bola:"))
pi = 3.14
circun = 2 * pi * raio



b1 = bola("azul",circun,"madeira")
b1.trocaCor()
b1.mostraCor()
