class Pessoa:
    ano_atual = 2022
    @classmethod
    def por_ano_nascimento(cls,nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        print(idade)


p1 = Pessoa.por_ano_nascimento('erick',2003)
p2 = Pessoa.por_ano_nascimento('ana',2004)
