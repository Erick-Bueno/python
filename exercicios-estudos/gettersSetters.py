class ficha:
    def __init__(self,nome):
        self.nome = nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
       for c in novo_nome:
           print(c)
           self._nome = novo_nome
       
       





    
p1 = ficha("erick")

        

