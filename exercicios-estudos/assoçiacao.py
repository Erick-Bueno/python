class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self.aulas = None #atributo vazio 
    
    
       
class Professor:
    def __init__(self,nome,materia):
        self.nome = nome
        self.materia = materia
    def aula(self):
        print("o professor",self.nomee,"esta dando sua aulade",self.materiaa)


class Professora:
    def aula(self):
        print("a professora esta dando aula")
        




aluno = Aluno("Erick")
professor = Professor("marcos","Matematica")
professora = Professora()





aluno.aulas = professora
aluno.aulas.aula()

