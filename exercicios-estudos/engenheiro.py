from Interfaces_em_python.interfaces.formas import formasInterface
from typing import Type
from Interfaces_em_python.terrenos.quadrado import Terreno_quadrado
class Eng:
    def __init__(self, nome):
        self.nome = nome
    def calcular_area(self, terreno: type[formasInterface]):
        area = terreno.get_area()
        return (f"{self.nome} disse q a a area calculada é de {area} ")


engenheiro = Eng("erick")
terreno = Terreno_quadrado(2)
engenheiro.calcular_area(terreno)