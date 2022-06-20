from clientesss import Clientes

class Contas(Clientes):
    def __init__(self, nome, cpf, saldo, limite):
        self.saldo = saldo
        self.limite = limite
        super().__init__(nome, 25, cpf)
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("o valor sacado por foi de", valor)
        else:
            print("erro saldo insuficiente para saque")
    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("o valor depositado por", self.nome,"foi de", valor)
        else:
            print("valor insuficiente para deposito")
    def consultarSaldo(self):
        print("o seu saldo é de", self.saldo)
