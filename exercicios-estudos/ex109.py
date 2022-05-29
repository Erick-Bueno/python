import moeda
p = float(input("digite um valor:"))
print(" a metade do numero {} é {}".format(moeda.moeda(p),moeda.moeda(moeda.metade(p))))
print("o dobro do numero {} é {}".format(moeda.moeda(p),moeda.moeda(moeda.dobro(p))))
print("o aumento de 10% de {} é {}".format(moeda.moeda(p),moeda.moeda(moeda.aumento(p))))
print("o desconto de 13% do numero {} é {}".format(moeda.moeda(p),moeda.moeda(moeda.desconto(p))))
