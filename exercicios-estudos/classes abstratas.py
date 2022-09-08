from abc import ABC, abstractmethod

class Classeabstrata(ABC): #quando quisermos fazer uma classe abstrata passamos como herança o ABC, para o python considerar como classe abstrata essa classe deve possuir no minimo um metodo abstrado

    #o metodo abstrato deve estar presente na classe filha
    @abstractmethod
    def metodoabstrato(self):
        pass
    #Classe abstratas q so possuem metodos abstratos são considerados como interfaces
    
class Filha(Classeabstrata):

    def apresentasmetodo(self):
        print(self.atributo)
  
    def metodoabstrato(self):
        print("implementando metodo abstrato")

filha = Filha()
filha.apresentasmetodo()
filha.metodo("estou aqui")
filha.metodoabstrato()


#gerara um erro pois classes abstratas n podem ser instanciadas
classabstract = Classeabstrata()
classabstract.metodo("fazendo algo")