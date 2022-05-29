par = 0
numero1 = int(input("digite um numero:"))
numero2 = int(input("digite um numero:"))
numero3 = int(input("digite um numero:"))
numero4 = int(input("digite um numero:"))
tupla = (numero1, numero2, numero3, numero4)
print("o numero 9 apareceu {} vezes".format(tupla.count(9)))
print("o numero 3 foi digitado pela primeira vez na posição {}".format(tupla.index(4)))
if numero1 %2 == 0:
    par = par + 1
if numero2 %2 == 0:
    par = par + 1
if numero3 %2 == 0:
    par = par + 1
if numero4 %2 == 0:
    par = par + 1
print("a quantidade de numeros pares foi de {}".format(par))

