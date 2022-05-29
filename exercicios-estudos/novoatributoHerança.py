class Animal:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
class gato(Animal):
    def __init__(self, nome, idade, pelo):#adicionando um novo atributo
        super().__init__(nome,idade) #indica que os atributos declarado na classe mãe irão ser usados, se n for colocado ao adicionar um novo atributo ira ocasionar erro
        self.pelo = pelo
    def miar(self):
        print(self.nome,"esta miando")
    def cor_pelo(self):
        print("a cor do pelo do",self.nome,"é", self.pelo)

gato1 = gato("gersu",2,"preto")
gato1.miar()
gato1.cor_pelo()
        
        