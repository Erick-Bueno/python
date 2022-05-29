


class Mae:
    def __init__(self,nome):
        self.nome = nome
        print("mamãe")
class pai:
    def __init__(self,nomee):
        self.nomee = nomee
        print("papai")
class filho(Mae, pai):
    def __init__(self):
        Mae.__init__(self, "sirlei")
        pai.__init__(self,"joseleno") #usar isso quando estiver usando herança multipla pois no super ele so ira retornar o primeiro metodo, ja com esse formato voce conseguira retornar todos os metodos
        print(self.nome, self.nomee)

f = filho()
