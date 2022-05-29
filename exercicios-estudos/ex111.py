import moeda
p = float(input("digite um valor:"))
print(" a metade do numero {} é {}".format(moeda.moeda(p),moeda.metade(p, False)))
print("o dobro do numero {} é {}".format(moeda.moeda(p),moeda.dobro(p, False)))
print("o aumento de 10% de {} é {}".format(moeda.moeda(p),moeda.aumento(p, False)))
