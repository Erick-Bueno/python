from interfaces.formas import formasInterface


class Terreno_quadrado(formasInterface):
    def __init__(self, lado):
        self.lado = lado

    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro
    def get_area(self):
        area = self.lado * self.lado
        return area        