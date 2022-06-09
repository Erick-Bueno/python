import datetime
hoje = datetime.date.today()
ano = hoje.year

class eu:
    def __init__(self,nome,nascimento):
        self.nome = nome
        self.nascimento = nascimento
    @property
    def nome (self):
        return self._nome
    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.replace("e",".")

    @property
    def nascimento (self):
        return self._nascimento
    @nascimento.setter
    def nascimento (self, valor):
        valor = ano- valor
        self._nascimento = valor




i = eu("erick",2003)
print(i.nome)
print(i.nascimento)

