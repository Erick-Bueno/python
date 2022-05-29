class animal:
    def __init__(self,classe,cor,tamanho,correndo = False,bebendo = False):
        self.classe = classe
        self.cor = cor
        self.tamanho = tamanho
        self.correndo = False
        self.bebendo = False
        print("o animal",self.classe,"tem a cor",self.cor,"e é do tamanho",self.tamanho)
    def especie(self,esp):
        print("O animal da classe",self.classe,"pertence a especie",esp)
        self.especie = esp
    def correr(self):
        if self.correndo == True:
            print (self.especie,"ja ta correndo")
            return
        print(self.especie,"esta correndo")
        self.correndo =True
    
    def parar_correr(self):
        if self.correndo == False:
            print(self.especie,"Ja esta parado")
            return
        print(self.especie,"parou de correr")
        self.correndo = False
    def beber(self):
        if self.correndo == True:
            print(self.especie,"não pode beber correndo")
            return
        print(self.especie,"da cor",self.cor,"ja pode beber")
        



a1 = animal("mamifero","preto","grande")
a2 = animal("mamifero","cinza","medio")
a1.especie("cachorro")
a2.especie("gato")

a1.correr()
a1.parar_correr()
a1.beber()

a2.correr()
a2.parar_correr()
a2.beber()






