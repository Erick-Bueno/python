

class Contas():
    def __init__(self, cliente, saldo, limite):
        self.saldo = saldo
        self.limite = limite
        self.cliente = cliente
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("o valor sacado por", self.cliente ,"foi de", valor)
        else:
            print("erro saldo insuficiente para saque")
    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("o valor depositado foi de ", valor)
        else:
            print("valor insuficiente para deposito")
    def consultarSaldo(self):
        print("o seu saldo é de", self.saldo)
