

class pessoas:
    def __init__(self,nome):
        self.nome = nome

        
class ficha:
    def __init__(self):
        self.fichaa = []

    def mostrar_ficha(self):
        for c in self.fichaa:
            print(c.nome)

    def inserir_na_ficha(self,nome):
        self.fichaa.append(nome)





fichario = ficha()
p1 = pessoas("erick")
p2 = pessoas("manel")




fichario.inserir_na_ficha(p1)
fichario.inserir_na_ficha(p2)
fichario.mostrar_ficha()




