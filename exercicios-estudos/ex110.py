import moeda
p = float(input("digite um valor:"))
print(" a metade do numero {} é {}".format(moeda.moeda(p),moeda.metade(p,True)))
print("o dobro do numero {} é {}".format(moeda.moeda(p),moeda.dobro(p, True)))
print("o aumento de 10% de {} é {}".format(moeda.moeda(p),moeda.aumento(p, False)))
print("o desconto de 13% do numero {} é {}".format(moeda.moeda(p),moeda.desconto(p, False)))
