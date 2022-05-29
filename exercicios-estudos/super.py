class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def pessoa_estudo(self):
        print(self.nome,"ta estudando")

class aluno(pessoa):
     def aluno_estuda(self):
         super().pessoa_estudo()



p1 = aluno('ana',18)
p1.aluno_estuda()
