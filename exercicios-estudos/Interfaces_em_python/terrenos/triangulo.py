from interfaces.formas import formasInterface

class triangulo(formasInterface):
    def __init__(self, lado1, lado2, lado3,base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def get_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro
    def get_area(self):
        area = (self.base * self.altura)/2
        return area
