
from clientes import Clientes
from contas import Contas


c1 = Clientes("erick", 1234530, 18)
conta1=Contas(c1,200,10)
conta1.depositar(3)
conta1.consultarSaldo()
conta1.sacar(200)
conta1.consultarSaldo()



