valor = int(input("qual numero voce gostaria de ver a tabuada:"))
calc = 0
for c in range(1, 11):
    calc = valor * c
    print(valor, "x", c, "=", calc)