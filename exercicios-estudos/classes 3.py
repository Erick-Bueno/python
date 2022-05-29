class acao:
    def __init__(self, nome, falando = False, caminhando = False):
        self.falando = falando
        self.caminhando = caminhando
        self.nome = nome
    def falar(self):
        if self.falando == True:
            print(self.nome,"ja esta falando")
            return
        print(self.nome,"esta falando algo")
        self.falando = True
    def andar(self):
        if self.caminhando == True:
            print(self.nome,"esta caminhando")
            return
        print(self.nome," esta parado")
        self.caminhando = True
    def parar_andar(self):
        if self.caminhando == False:
            print(self.nome,"não esta andando")
            return
        print(self.nome,"parou de andar")
        
            


p1 = acao("erick")
p1.falar()
p1.parar_andar()
p1.falar()
p1.andar()
p1.andar()
p1.parar_andar()

