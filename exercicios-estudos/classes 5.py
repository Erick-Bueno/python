class Pessoa:
    def __init__(self,nome, jogando = False, estudando = False):
        self.nome = nome
        self.jogando = jogando
        self.estudando = estudando
    def jogar(self):
        if self.jogando == True:
            print("ja esta jogando")
            return
        print(self.nome,"esta jogando")
        self.jogando = True
    def parar_jogar(self):
        if self.jogando == False:
            print(self.nome,"não esta jogando")
            return
        print(self.nome,"parou de jogar")
        self.jogando = False
   
       
            

    

p1 = Pessoa("Erick")
p1.jogar()
p1.parar_jogar()









