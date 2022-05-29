class acao:
    def __init__(self, nome, falando = False, caminhando = False):
        self.falando = falando
        self.caminhando = caminhando
        self.nome = nome
    def caminhar(self,andar):
        print(self.nome,"esta",andar)
        self.caminhando = True
    def falar(self):
        if self.caminhando == True:
            print(self.nome,"não pode falar")
    def parou_caminhar(self):
        print(self.nome,"parou de caminhar")
        self.caminhando = False
    def pode_falar(self):
        if self.caminhando == False:
            print(self.nome,"começa a falar")
            self.falando = True
            return
        if self.falando == True:
            print("ja esta falando")
        
            
        
p1 = acao("erick")
p1.caminhar("caminhando")
p1.falar()
p1.parou_caminhar()
p1.pode_falar()
p1.pode_falar()
