class imprimir:
    a = 10
    def folhas(self, paginas):
        print("chamando metodo de instancia")
        for c in range(0, paginas):
            print("imprindo folha")
        self.impressao()
    def paragrafo(self):
        print("2 pargrafos")
        self.imprimir_a()
    @classmethod
    def imprimir_a(cls):
        print("chamando metodo de classe")
        print(cls.a)
        #POSSO USAR METODO ESTATICO NO METODO DE CLASSE
        cls.impressao()
        
        

    @staticmethod
    def impressao():
        print("ola mundo")
        

#chamar metodo de classe
imprimir.imprimir_a()

f1 = imprimir()
f1.folhas(5)


imprimir.impressao()

f1.paragrafo()

        
            




