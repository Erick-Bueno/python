class ficha:
    nome = "gabriel"
    idade = 19
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura= altura
        self.peso = peso
        #exemplo de metodo de instancia
    def imc(self):
        IMC = self.peso/(self.altura*self.altura)
        print("o imc de",self.nome,"vale",IMC)
        
        #exemplo de metodo de classe
    @classmethod
    def numero_pessoas(cls,quant):
        for c in range(0,quant):
            print(cls.nome,"de idade",cls.idade,"anos se cadastrou(ram)")

    @staticmethod
    def sexo():
            print(ficha.idade *2)
           
    @classmethod
    def alterar_nome(cls,nova_idade):
        ficha.idade= nova_idade 
        print(ficha.idade)
   
            
        
    



print("dobro da idade")
ficha.sexo()
print("nova idade")
ficha.alterar_nome(10)
print("dobro da nova idade")
ficha.sexo()





















